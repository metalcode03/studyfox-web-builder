from django.db import models
from django.db.models.fields import related

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Departments'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.department

class Class(models.Model):
    clas = models.CharField(max_length=300)

    class Meta:
        verbose_name='Classes'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.klass

class Subject(models.Model):
    subject = models.CharField(max_length=300)
    klass = models.ForeignKey(Class, related_name='select_a_class', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Subjects'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject
