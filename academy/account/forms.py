from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.utils.safestring import mark_safe

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label=mark_safe('<b>pochta</b>'))
    username=forms.CharField(help_text=False,label=mark_safe('<b>Ism</b>'))
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image=forms.ImageField(help_text=False,label=mark_safe('<b>Profile rasmi</b>'))
    
    class Meta:
        model = Profile
        fields = ['image']
        