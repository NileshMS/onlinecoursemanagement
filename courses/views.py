from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views he
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .forms import CustomUserCreationForm, AddCourseForm, EnrolModelForm
from .models import Course, ProfileModel, CustomUserModel, EnroledCourseModel


class SignUpVeiw(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'courses/studentssignup.html'
    success_message = 'welcome, Now you can login '


class CoursesListView(ListView):
    model = Course
    template_name = 'home.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/coursedetail.html'
    redirect_url = reverse_lazy('home')


# ________________ admin actions-------------------
class AdminHome(LoginRequiredMixin, ListView):
    model = CustomUserModel
    template_name = 'adminhome.html'
    login_url = 'login'
    redirect_field_name = 'login'
    context_object_name = 'users_list'
    ordering = ['-id']


class CreateNewCourse(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Course
    form_class = AddCourseForm
    template_name = 'courses/newcourse.html'
    success_url = reverse_lazy('course_list_view')
    success_message = 'New course is added'
    login_url = 'login'
    redirect_field_name = 'login'


class CourseList(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/course_list.html'
    login_url = 'login'
    redirect_field_name = 'login'


class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = AddCourseForm
    template_name = 'updatecourse.html'
    success_url = reverse_lazy('course_list_view')
    login_url = 'login'
    redirect_field_name = 'login'


class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'coursedelete.html'
    success_url = reverse_lazy('course_list_view')
    login_url = 'login'
    redirect_field_name = 'login'


class ProfileView(LoginRequiredMixin, ListView):
    model = ProfileModel
    template_name = 'courses/profilemodel_list.html'
    login_url = 'login'
    redirect_field_name = 'login'


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = CustomUserModel
    template_name = 'adminhome.html'
    success_url = reverse_lazy('adminhome')
    login_url = 'login'
    redirect_field_name = 'login'


class Enroll(LoginRequiredMixin, CreateView):
    model = EnroledCourseModel
    form_class = EnrolModelForm
    template_name = 'courses/profilemodel_list.html'
    success_url = 'profile'


# class EnrolledCourses(LoginRequiredMixin, ListView):
#     model = EnroledCourseModel
#     template_name = 'adminhome.html'
#     context_object_name = 'objects'

def enroledcourse(request):
    objects = EnroledCourseModel.objects.filter()
    for x in objects:
        print(x)
    return render(request, 'adminhome.html', {'objects':objects} )