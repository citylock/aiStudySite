from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(ModelForm):
    #  회원 가입 형식 
    password_check =  forms.CharField(max_length=100, widget=forms.PasswordInput())
    field_order = ['username', 'password', 'password_check', 'last_name', 'first_name', 'email']

    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput }
        fields = ['username', 'password', 'last_name', 'first_name', 'email']

class SigninForm(ModelForm):
    class Meta: 
        model = User
        widgets = {'password': forms.PasswordInput }
        fields = ['username', 'password']
