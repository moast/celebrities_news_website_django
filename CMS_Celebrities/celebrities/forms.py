from django.contrib.auth.models import User
from django import forms




class UserLoginForm(forms.Form):
      username = forms.CharField()
      password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterFrom(forms.ModelForm):
      password = forms.CharField(widget=forms.PasswordInput)

      class Meta:
           model = User
           fields = ["username","password"]