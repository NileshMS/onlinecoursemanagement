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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.CoursesListView.as_view(), name='home'),
    # path('', views.course_list, name='home'),
    # --------------------admin course create,read, update, delete-----------------
    path('adminhome/', views.AdminHome.as_view(), name='adminhome'),
    path('newcourse/', views.CreateNewCourse.as_view(), name='newcourse'),
    path('courselist/', views.CourseList.as_view(), name='course_list_view'),
    # path('courselist/', views.course_list_view, name='course_list_view'),
    path('courseupdate/<int:pk>/', views.CourseUpdate.as_view(), name='courseupdate'),
    path('deletecourse/<int:pk>/', views.CourseDelete.as_view(), name='coursedelete'),

    # -------------------signup, login, logout-------------------
    path('signup/', views.SignUpVeiw.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='courses/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='courses/logout.html'), name='logout'),

    # --------------Authentication-------------------------------
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='change_password'),
    path('change_password_done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='change_password_done'),

    # -------------------Profile----------------------------
    path('profile/',views.ProfileView.as_view(), name='profile'),
]
