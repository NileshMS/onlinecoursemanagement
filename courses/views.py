from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Course
# Create your views here.
from .forms import CustomUserCreationForm, UserChangeForm

class SignUpVeiw(CreateView):
    form_class= CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'courses/studentssignup.html'


class CoursesListView(ListView):
    model = Course
    template_name = 'home.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/coursedetail.html'

# ________________ admin actions-------------------
class AdminHome(TemplateView):
    template_name = 'adminhome.html'

class CreateNewCourse(CreateView):
    model = Course
    template_name = 'adminhome.html'
    success_url = 'adminhome'

class CourseList(ListView):
    model = Course
    template_name = 'adminhome.html'

class CourseUpdate(UpdateView):
    model= Course
    template_name = 'updatecourse.html'
    redirect_url= reverse_lazy('adminhome')

class CourseDelete(DeleteView):
    model = Course
    template_name = 'coursedelete.html'
    redirect_url = reverse_lazy('adminhome')
