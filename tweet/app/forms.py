from django import forms
from .models import TweetModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#create your forms here

class TweetCreateForm(forms.ModelForm):
    class Meta:
        model=TweetModel
        fields=['photo','description']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    model=User()
    fields=('username','email','password1','password2')