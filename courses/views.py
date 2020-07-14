from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, ProfileModel, CustomUserModel, EnroledCourseModel
# Create your views here.
from .forms import CustomUserCreationForm, AddCourseForm


class SignUpVeiw(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'courses/studentssignup.html'


class CoursesListView(ListView):
    model = Course
    template_name = 'home.html'
    context_object_name = 'courses'

# def course_list(request):
#     course = Course.objects.all()
#     print(course)
#     return render(request, 'home.html', {'courses': course})


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/coursedetail.html'
    redirect_url = reverse_lazy('home')


# ________________ admin actions-------------------
class AdminHome(TemplateView):
    template_name = 'adminhome.html'


class CreateNewCourse(CreateView):
    model = Course
    form_class = AddCourseForm
    template_name = 'courses/newcourse.html'
    success_url = reverse_lazy('course_list_view')


class CourseList(ListView):
    model = Course
    template_name = 'courses/course_list.html'


class CourseUpdate(UpdateView):
    model = Course
    form_class = AddCourseForm
    template_name = 'updatecourse.html'
    success_url = reverse_lazy('course_list_view')


class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'coursedelete.html'
    success_url = reverse_lazy('course_list_view')

class ProfileView(ListView):
    model = ProfileModel
    template_name = 'profile.html'
