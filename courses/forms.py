from django  import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= CustomUserModel
        fields= ['username', 'email', 'phone']

class CustomUserChangeForm(UserChangeForm):
    # A form used in the admin interface to change a user’s information and permissions
    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'phone']