from django.shortcuts import render
from .models import *

# Create your views here.


def index(request, slug):
    school = School.objects.get(slug=slug)
    school_home = SchoolHomePage.objects.get(school=school)
    # school_achievement = SchoolAchievement.objects.get(school=school)
    # personals = Personals.objects.get(school=school)
    # singlefeature = SingleFeature.objects.get(personal=personals)
    codex = 1
    context = {
        'school': school,
        'school_home': school_home,
        'codex': codex
    }
    return render(request, f'school/temp/{school.template_path}/index.html', context)


def aboutus(request, slug):
    school = School.objects.get(slug=slug)
    school_home = SchoolHomePage.objects.get(school=school)
    # school_achievement = SchoolAchievement.objects.get(school=school)
    personals = Personals.objects.get(school=school)
    aboutschool = AboutSchool.objects.get(school=school)
    singlefeature = SingleFeature.objects.filter(personal=personals)
    schoolteacher = SchoolTeacher.objects.filter(school=school)
    context = {
        'about': aboutschool,
        'school': school,
        'school_home': school_home,
        'schoolteacher': schoolteacher,
        'personals': personals,
        'singlefeature': singlefeature[:5],
    }
    return render(request, f'school/temp/{school.template_path}/aboutus.html', context)
