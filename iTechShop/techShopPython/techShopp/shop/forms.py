from django import forms
from .models import Customer
import datetime

def inputText(attr):
        classCss = forms.TextInput(attrs={
            'class':"form-control",
            'placeholder':attr,
            'maxlength':100
        })
        return classCss

def inputHidden(attr):
        classCss = forms.HiddenInput(attrs={
            'class': "form-control",
            'placeholder': attr,
            'maxlength': 100
        })
        return classCss


def inputTextarea(attr):
    classCss = forms.Textarea(attrs={
        'class': "form-control",
        'placeholder': attr,
    })
    return classCss

class CustomerForm(forms.ModelForm):
    name = forms.CharField(label='name',widget=inputText("Nhập họ tên"))
    mobile = forms.CharField(label='mobile', widget=inputText("Nhập điện thoại"))
    email = forms.CharField(label='email', widget=inputText("Nhập thư điện tử"))
    address = forms.CharField(label='address', widget=inputText("Nhập địa chỉ"))
    class Meta:
        model = Customer
        fields = "__all__"

