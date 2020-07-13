from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here
class CustomUserModel(AbstractUser):
    phone = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.username


class ProfileModel(models.Model):
    student_profile = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_profile.username} Profile!!'


class Course(models.Model):
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


class EnroledCourseModel(models.Model):
    course_profile = models.ManyToManyField(Course, on_delete=models.CASCADE)
    student = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
