from django.db import models
from accounts.models import Profile
from school_app.models import School
from django.utils import timezone


class Student(models.Model):
    students = models.OneToOneField(Profile, on_delete=models.CASCADE)
    school = models.ForeignKey(
        School, on_delete=models.DO_NOTHING, blank=True, unique=False)
    studentid = models.CharField(unique=True, max_length=20, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Students'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.students.user.username


class StudentID(models.Model):
    studentid = models.CharField(max_length=15, unique=True, blank=False)
    school = models.ForeignKey(
        School, on_delete=models.DO_NOTHING, unique=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.studentid
