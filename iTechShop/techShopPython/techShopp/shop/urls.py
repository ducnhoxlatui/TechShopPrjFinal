from django import urls
from django.urls import path
from django.urls import path
from  .views import *
from django.contrib.auth.views import LogoutView




from . import views
urlpatterns = [
    path('detail/<int:p_id>', views.product_detail, name='Pdetail'),
    path('', indexx.as_view(),name='index'),
    path('product', views.product_detail,name='product_detail'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('register/',RegisterFage.as_view(),name='register'),
    path('shop/addcart', addcart, name='buyproduct'),
    path('customerpage/', customerpage, name='customerpage'),
    path('search/', SearchResultsView.as_view(),name = 'search_results')

]
