from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class CreateUserForm(UserCreationForm):
  class Meta:
    model=User
    fields=['username','email','password1','password2']
class adminproduct(forms.ModelForm):
    class Meta:
       model = Product
       fields = ['name','content','category','ram','price','storage','index','image','price2']
       widgets ={
          'name':forms.TextInput(attrs={'class':'form-control'}),
          'content':forms.TextInput(attrs={'class':'form-control'}),
          'category':forms.Select(attrs={'class':'form-control'}),
          'ram':forms.NumberInput(attrs={'class':'form-control'}),
          'price':forms.NumberInput(attrs={'class':'form-control'}),
          'storage':forms.NumberInput(attrs={'class':'form-control'}),
          'index':forms.Select(attrs={'class':'form-control'}),
          'image':forms.FileInput(attrs={'class':'form-control'}),
          'price2':forms.NumberInput(attrs={'class':'form-control'}),


       }

class reviewss(forms.ModelForm):
    class Meta:
       model = review
       fields = ['text']
       widgets ={
          'text':forms.TextInput(attrs={'class':'input'}), 
       }
       labels={
          'text':'add a comment'
       }