from django.urls import path
from . import views as v

app_name = 'main'

urlpatterns = [
    path('', v.index, name='index'),
    path('aboutus', v.aboutus, name='about'),
    path('choice/preference/', v.preference, name='preference'),
    # path('school/pass', v.passer, name='passer'),
    path('school/registration', v.school_registration, name='school_reg'),
    path('school/registration/<int:pk>', v.SchoolRegView.as_view(), name='continue_reg'),
    path('school/course/secondary', v.course, name='course'),
    path('school/course/secondary/ss1', v.class_detail, name='class_detail'),
]
