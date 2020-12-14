from django.urls import path

from . import views as v

app_name = 'schoolapp'

urlpatterns = [
    path('', v.index, name='index'),
    path('about', v.aboutus, name='about'),
]
