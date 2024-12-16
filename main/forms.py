from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    admin_code = forms.CharField(
        max_length=10, 
        required=True, 
        widget=forms.PasswordInput,
        label='Admin Code'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role', 'admin_code']
