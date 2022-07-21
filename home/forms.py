from django.forms import fields
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserChangeForm
from home.models import City, Hotel, Cart, UserDetail



class CustomerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}


# class ProfileRegistrationForm(forms.ModelForm):
#         class Meta:
#             model = Profile
#             fields = ['age', 'cnic']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=("password"), strip=False, widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password', 'class': 'form-control'}))


class EditChangeForm(UserChangeForm):
    password = None
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}


class DetailForm(forms.ModelForm):
   class Meta:
       model = UserDetail
       fields = '__all__'
       widgets = {
           'na': forms.TextInput,
           'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter first Name'}),
           'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter last Name'}),
           'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter phone number '}),
           'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter notes here'}),
           'email': forms.EmailInput(attrs={'class': 'form-control'}),

       }
