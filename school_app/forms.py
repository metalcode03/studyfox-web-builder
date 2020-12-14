from django import forms

from .models import (
    AboutSchool,
    School,
    SchoolAchievement,
    SchoolService,
    SchoolHomePage,
    SchoolTestimonial
)


class SchoolRegForm(forms.ModelForm):

    class Meta:
        model = School
        fields = [
            'name',
            'logo',
        ]
        

class SchoolRegForm2(forms.ModelForm):

    class Meta:
        model = School
        fields = [
            'description'
        ]
        
        
