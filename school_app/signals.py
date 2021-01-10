from django.db.models.signals import post_save
from django.dispatch import receiver

from school_app.models import (
    School, 
    SchoolHomePage,
    SchoolAchievement,
    SchoolInformation,
    SchoolNews,
    SchoolService,
    SchoolTeacher,
    SchoolTestimonial,
    SingleFeature,
    SocialLink,
    Personals
)


# @receiver(post_save, sender=School)
