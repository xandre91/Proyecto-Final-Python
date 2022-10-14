from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_user(forms.Form):
    name = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=30)
    email = forms.EmailField()

class form_driver(forms.Form):
    name = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=30)
    email = forms.EmailField()
    registry = forms.IntegerField()

class form_movile(forms.Form):
    carPatent = forms.CharField(max_length=30)
    carBrand = forms.CharField(max_length=30)
    year = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput())
    password2 = forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

