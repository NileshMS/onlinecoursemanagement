"""onlinecoursemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from courses import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('course_list/',views.CoursesListView.as_view(template_name='home.html'), name='course_list'),

    #--------------------admin course create,read, update, delete-----------------
    path('adminhome', views.AdminHome.as_view(), name='adminhome'),
    path('newcourse', views.CreateNewCourse.as_view(), name='newcourse'),
    path('courselist', views.CourseList.as_view(), name='courselist'),
    path('updatecourse', views.CourseUpdate.as_view(), name='courseupdate'),
    path('deletecourse', views.CourseDelete.as_view(), name='coursedelete'),



    # -------------------signup, login, logout-------------------
    path('signup/', views.SignUpVeiw.as_view(), name='signup'),
    path('login/',LoginView.as_view(template_name='courses/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='courses/logout.html'), name='logout'),

    # --------------Authentication-------------------------------



]
