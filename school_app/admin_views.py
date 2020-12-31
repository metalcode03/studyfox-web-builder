from datetime import datetime
# class based views
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# modules
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.safestring import mark_safe

# Installed apps modules
from main.utils import Calendar
from main.models import Event

# Local modules
from .models import *

# Create your views here.




class DashboardView(ListView):
    model = School
    template_name = 'school/school_admin/admin.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        # context['prev_month'] = prev_month(d)
        # context['next_month'] = next_month(d)
        return context


class CalendarView(ListView):
    model = Event
    template_name = 'components/calendar.html'
    success_url = reverse_lazy("calendar")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        # context['prev_month'] = prev_month(d)
        # context['next_month'] = next_month(d)
        return

# Form Class Based Views

class EventEditView(UpdateView):
    model = Event
    fields = ['description']
    template_name = 'school/school_registration/cont_form.html'
    success_url = '/'


class SchoolHomeEditView(UpdateView):
    model = SchoolHomePage
    fields = [
        'hero_title',
        'hero_text',
        'hero_image',
    ]
    success_url = '/'

    def get_queryset(self):
        model = self.model
        school = School.objects.filter(slug=self.kwargs['slug'])
        # model.filter(school)
        return school


class SchoolWebEditView(DetailView):
    model = School
    template_name = 'school/school_admin/forms/webform.html'


# Function Based Views

def dashboard(request, slug):
    school = School.objects.get(slug=slug)
    return render(request, 'school/school_admin/admin.html')


def student_list(request, slug):
    school = School.objects.get(slug=slug)
    return render(request, 'school/school_admin/lists.html')


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()
