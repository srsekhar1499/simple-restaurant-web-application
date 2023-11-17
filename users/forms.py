from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Meta class you about the Present class
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
        
