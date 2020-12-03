from django.urls import path
from . import views as v

app_name = 'main'

urlpatterns = [
    path('', v.index, name='index'),
    path('choice/preference/', v.preference, name='preference')
]
