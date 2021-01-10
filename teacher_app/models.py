from django.db import models
from accounts.models import User
from school_app.models import School
from class_app.models import Class, Subject

# Create your models here.
class Worker(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.OneToOneField(School, on_delete=models.CASCADE, blank=True, null=True)
    klass = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name="select_class", blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Workers'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.person.username
