from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('username', 'email')
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')

# class FormFormView(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = '__all__'
#         # fields = ('title', 'content', 'created_at', 'updated_at', 'photo', 'is_published')