from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SportForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['name', 'position', 'team', 'country', 'description', 'goals', 'assists', 'player_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
