# class based views
from django.views.generic.edit import UpdateView
# modules
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib import messages
from school_app.models import School
from school_app.forms import SchoolRegForm, SchoolRegForm2
from accounts.models import User

def index(request):
    return render(request, 'home/index.html')

def preference(request):
    return render(request, 'main/preference.html')

def aboutus(request):
    return render(request, 'main/about.html')


def passer(request):
    return render(request, 'school/school_admin/admin.html')

def success_message(request):
    return render(request, 'school/school_registration/congrats.html')


def school_registration(request):
    if request.method == 'POST':
        form = SchoolRegForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.maintainer = request.user
            data.save()
            return redirect('schoolapp:course')
    form = SchoolRegForm()
    context = {
        'form': form
    }
    return render(request, 'school/school_registration\school_form1.html', context)


class SchoolRegView(UpdateView):
    model = School
    fields = ['description']
    template_name = 'school/school_registration/cont_form.html'
    success_url = '/'


def course(request):
    return render(request, 'school/school_admin/course/course.html')


def class_detail(request):
    return render(request, 'school/school_admin/course/class_detail.html')
