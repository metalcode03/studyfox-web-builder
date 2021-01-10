from django.urls import path
from . import views as v

app_name = 'main'

urlpatterns = [
    path('', v.index, name='index'),
    path('aboutus', v.aboutus, name='about'),
    path('service', v.service, name='service'),
    path('pricing', v.pricing, name='pricing'),
    path('contact-us', v.contactus, name='contact-us'),
    path('choice/preference/', v.preference, name='preference'),
    # path('school/pass', v.passer, name='passer'),
    path('school/registration', v.school_registration, name='school_reg'),
    path('school/registration/personal/<int:id>', v.update_personal, name='personal_reg'),
    path('school/registration/<int:pk>', v.SchoolRegView.as_view(), name='domain_reg'),
    path('school/registration/congrats',v.success_message, name='success_message'),
    path('school/course/secondary', v.course, name='course'),
    path('school/course/secondary/ss1', v.class_detail, name='class_detail'),
]
