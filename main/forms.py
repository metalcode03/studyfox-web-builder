from django import forms

from accounts.models import Profile, User

class PersonalRegForm(forms.ModelForm):
    are_you_admin = forms.BooleanField()
    
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'other_name',
            'gender',
            'address',
            'state',
            'country',
        ]

