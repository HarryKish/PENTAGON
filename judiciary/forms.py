from django import forms
from . models import Criminal
from django.contrib.auth.models import User


class CriminalForm(forms.ModelForm):
     class Meta:

        model = Criminal
        fields = '__all__'

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
