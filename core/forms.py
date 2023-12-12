from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', 
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password', 
        'class': 'w-full py-4 px-6 rounded-xl'
    }))     

class SignupForm(UserCreationForm):
    class Meta:
        
        # it automatically linked with User Model
        model = User

        # The fields you need for your form, and Django will generate the corresponding form fields for those model fields.
        fields = ('username', 'email', 'password1', 'password2') 
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', 
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email', 
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password', 
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password', 
        'class': 'w-full py-4 px-6 rounded-xl'
    }))    