from django.contrib import admin
from .models import Course, ProfileModel, CustomUserModel, EnroledCourseModel
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Course)
admin.site.register(ProfileModel)
admin.site.register(EnroledCourseModel)
# admin.site.register(CustomUserModel)

from .forms import CustomUserCreationForm, CustomUserChangeForm



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel

admin.site.register(CustomUserModel, CustomUserAdmin)
