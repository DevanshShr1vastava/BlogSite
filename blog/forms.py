from django import forms
from .models import BlogPost

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category']



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Provide a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
