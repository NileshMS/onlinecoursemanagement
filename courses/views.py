from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
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
    paginate_by = 3
    context_object_name = 'courses_list'


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
    success_url = 'adminhome'

# class CourseList(ListView):
#     model = Course
#     template_name = 'courses/course_list.html'

def course_list_view(request):
    courses = Course.objects.all()
    print(courses)
    return render(request, 'courses/course_list.html', {'objects_list': courses})

class CourseUpdate(UpdateView):
    model = Course
    form_class = AddCourseForm
    template_name = 'updatecourse.html'
    redirect_url = reverse_lazy('adminhome')


class CourseDelete(DeleteView):
    model = Course
    template_name = 'coursedelete.html'
    redirect_url = reverse_lazy('adminhome')
