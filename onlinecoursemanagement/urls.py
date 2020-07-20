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
from django.views.generic import DeleteView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView,PasswordChangeForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CoursesListView.as_view(), name='home'),
    path('coursedetail/<int:pk>/', views.CourseDetailView.as_view(), name='coursedetail'),
    # --------------------admin course create,read, update, delete-----------------
    path('adminhome/', views.AdminHome.as_view(), name='adminhome'),
    path('deleteuser/<int:pk>/',views.DeleteUserView.as_view(), name='delete_user'),
    path('newcourse/', views.CreateNewCourse.as_view(), name='newcourse'),
    path('courselist/', views.CourseList.as_view(), name='course_list_view'),
    path('courseupdate/<int:pk>/', views.CourseUpdate.as_view(), name='courseupdate'),
    path('deletecourse/<int:pk>/', views.CourseDelete.as_view(), name='coursedelete'),

    # -------------------signup, login, logout-------------------
    path('signup/', views.SignUpVeiw.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='courses/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='courses/logout.html',redirect_field_name='home'), name='logout'),

    # --------------Authentication-------------------------------
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name='change_password.html', form_class =PasswordChangeForm), name='change_password'),
    path('change_password_done/',PasswordChangeDoneView.as_view(template_name='password_change_done.html' ), name='password_change_done'),

    # -------------------Profile----------------------------
    path('profile/',views.ProfileView.as_view(), name='profile'),
    # path('enrolledcourses/<int:pk>/', views.EnrolledCourses.as_view(), name='enrolledcourses'),
    path('enrolledcourses/<int:pk>/', views.enroledcourse, name='enrolledcourses'),
    path('enroll/<int:pk>/', views.Enroll.as_view(), name='enroll'),
]
