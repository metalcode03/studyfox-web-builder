from datetime import datetime
# class based views
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
# modules
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe

# Installed apps modules
from main.utils import Calendar
from main.models import Event

# Local modules
from .models import *

# Create views for school website.
def index(request, slug):
    school = School.objects.get(slug=slug)
    school_home = SchoolHomePage.objects.get(school=school)
    # school_achievement = SchoolAchievement.objects.get(school=school)
    schooltestimony = SchoolTestimonial.objects.filter(school=school)
    personals = Personals.objects.get(school=school)
    singlefeature = SingleFeature.objects.filter(personal=personals)
    schoolinfo = SchoolInformation.objects.get(school=school)
    social_link = SocialLink.objects.filter(school_info=schoolinfo)
    school_service = SchoolService.objects.filter(school=school)
    school_news = SchoolNews.objects.filter(school=school)
    codex = 1
    context = {
        'school': school,
        'school_home': school_home,
        'school_service': school_service,
        'codex': codex,
        'social_link': social_link,
        'schoolinfo': schoolinfo,
        'personals': personals,
        'singlefeature': singlefeature[:5],
        'schooltestimony': schooltestimony[:3],
        'school_news': school_news[:3],
    }
    return render(request, f'school/temp/{school.template_path}/index.html', context)


def aboutus(request, slug):
    school = School.objects.get(slug=slug)
    school_home = SchoolHomePage.objects.get(school=school)
    # school_achievement = SchoolAchievement.objects.get(school=school)
    personals = Personals.objects.get(school=school)

    aboutschool = AboutSchool.objects.get(school=school)
    singlefeature = SingleFeature.objects.filter(personal=personals)

    schoolinfo = SchoolInformation.objects.get(school=school)
    social_link = SocialLink.objects.filter(school_info=schoolinfo)

    schoolteacher = SchoolTeacher.objects.filter(school=school)
    context = {
        'about': aboutschool,
        'schoolinfo': schoolinfo,
        'school': school,
        'school_home': school_home,
        'schoolteacher': schoolteacher,
        'social_link': social_link,
        'personals': personals,
        'singlefeature': singlefeature[:5],
    }
    return render(request, f'school/temp/{school.template_path}/aboutus.html', context)
