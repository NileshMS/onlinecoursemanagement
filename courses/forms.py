from django  import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

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

from .models import Course


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_fee(self):
        fee = self.cleaned_data['fee']
        if fee >= 3000:
            return fee
        else:
            raise ValidationError('Fee must be greater than 3000..')
