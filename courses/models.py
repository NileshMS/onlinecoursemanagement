from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here
class CustomUserModel(AbstractUser):
    phone = models.PositiveIntegerField(unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username


class Course(models.Model):  # publicatins
    courseid = models.AutoField(primary_key=True)
    course = models.CharField(max_length=60)
    faculty = models.CharField(max_length=50)
    content = models.TextField(max_length=250)
    date = models.DateField()
    time = models.CharField(max_length=20)
    fee = models.IntegerField()
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.course


class ProfileModel(models.Model):
    student_profile = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_profile.username} Profile!!'


class EnroledCourseModel(models.Model):  # article
    course_profile = models.ManyToManyField(Course, blank=True)
    student = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
