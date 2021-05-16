from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.edit import  FormView
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from .forms import CustomerForm


# Create your views here.



class indexx(View):
    def get(self,request):
        list_product = Product.objects.all()
        pg_list = PGroup.objects.all()
        br_list = Brand.objects.all()
        context = {'product_list': list_product,'pg_list':pg_list,'br_list':br_list}
        model = Product
        # Overrice lai ten cua object, mac dinh se la oject_list
        context_object_name = 'Product'
        fields = '__all__'
        return render(request,'shop/index.html',context)
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['Product']=context['Product'].filter(user=self.request.user)
        #Dem task chua thuc hien
        search_input =self.request.GET.get('search-area') or ''
        if search_input:
            context['Product']= context['Product'].filter(title__icontains=search_input)
        context['search-input'] =search_input
        return context


def product_detail(request,p_id):

    p = Product.objects.get(pk=p_id)
    return render(request, 'shop/product-detail.html', {'p': p})


class CustomLoginView(LoginView):
    #overrice lai ten template su dung mac dinh
    template_name = 'shop/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    # Dia chi tra ve khi thanh cong
    def get_success_url(self):
        return reverse_lazy('index')

class RegisterFage(FormView):
    # Overrice ten template mac dinh
    template_name ='shop/register.html'
    #Su dung form userceation form
    form_class = UserCreationForm
    redirect_authenticated_user = True
    # Dia chi dan toi khi thanh cong
    success_url = reverse_lazy('login')
    #Kiem tra hop le cua du lieu nhap vao
    def form_valid(self, form):
        # neu hop le thi luu vao database
        user =form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterFage,self).form_valid(form)
    # Kiem tra neu da co dang nhap roi thi truy cap vao trang task
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterFage,self).get(*args,**kwargs)

cart = {}

def addcart(request):
    if request.is_ajax():
        id = request.POST.get('id')
        num = request.POST.get('num')


        proDetail = Product.objects.get(pro_id=id)
        if id in cart.keys():
            itemCart = {
                'name': proDetail.pro_name,
                'price': proDetail.pro_price,
                'image': str(proDetail.pro_image),
                'num': int(cart[id]['num']) + 1
            }
        else:
            itemCart = {
                'name': proDetail.pro_name,
                'price': proDetail.pro_price,
                'image': str(proDetail.pro_image),
                'num': num
            }
        cart[id] = itemCart
        request.session['cart'] = cart
        cartInfo = request.session['cart']
        html = render_to_string('shop/addcart.html', {'cart': cartInfo})
    return HttpResponse(html)


# def shoppingcart(request):
#
#     return render(request,'shop/shoppingcart.html',{'form':form})


def customerpage(request):

    total = 0;
    carts = request.session['cart']
    for key,value in carts.items():
        total += int(value['price'])*int(value['num'])


    if request.method =="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            form = Customer(name=name,mobile=mobile,email=email,address=address)
            form.save()

    form = CustomerForm()

    return  render(request,'shop/customerpage.html',{'total':total,'form':form})

class SearchResultsView(ListView):
    model = Product
    template_name = 'shop/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        Psearch_list = Product.objects.filter(
            Q(pro_name__icontains=query) | Q(brand__name__icontains=query)
        )
        return Psearch_list


