from django.urls import path

from . import views as v, admin_views as a

app_name = 'schoolapp'

urlpatterns = [
    path('', v.index, name='index'),
    path('about', v.aboutus, name='about'),
    path('admin', a.dashboard, name='dashboard'),
    path('students/lists', a.student_list, name='student_list'),
    path('dashboard/', a.DashboardView.as_view(), name='dashboard'),
    path('dashboard/edit/', a.SchoolWebEditView.as_view(), name='web_edit_form'),
    path('eventthatidontwantanybodytogoto/<int:id>', a.EventEditView.as_view(), name='event_edit'),
]
