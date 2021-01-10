from django.core.checks import messages
from django.db import models
from django.db.models.fields import related
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from accounts.models import User



class School(models.Model):
    # admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=40, blank=True)
    logo = models.ImageField(upload_to='profilio/logo', blank=True)
    description = models.TextField(blank=True)
    registeration_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_on = models.DateField(blank=True, null=True)
    on_trial = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    template_path = models.CharField(
        max_length=30, blank=True, default='default')
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Schools'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_index_url(self):
        return reverse("schoolapp:index", kwargs={
            'slug': self.slug
        })


class SchoolHomePage(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    hero_title = models.CharField(max_length=40, blank=True)
    hero_text = models.TextField(blank=True)
    hero_image = models.ImageField(
        upload_to='school/hero_image', blank=True
    )

    class Meta:
        verbose_name_plural = 'School Home'

    def __str__(self):
        return self.hero_title


class SchoolAchievement(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    registered_students = models.PositiveIntegerField(blank=True, null=True)
    qualified_teachers = models.PositiveIntegerField(blank=True, null=True)
    graduated_students = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "School's Achievements"

    def __str__(self):
        return self.school.name


class SchoolTestimonial(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    image = models.ImageField(upload_to='school/testimonial/image', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "School's Testimonials"

    def __str__(self):
        return self.name


class AboutSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to='school/feature/image', blank=True)
    about = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'School About'

    def __str__(self):
        return self.subtitle


class SchoolService(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to='school/service/image', blank=True)
    description = models.TextField(blank=True)
    size_of_card = models.CharField(blank=True, max_length=10)
    icon = models.CharField(blank=True, max_length=53)
    code = models.CharField(blank=True, max_length=3)
    tag = models.CharField(blank=True, max_length=10)

    class Meta:
        verbose_name_plural = 'School Service'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='school/gallery/', blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Schools Gallery'

    def __str__(self):
        return self.title


class ContactSchool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=False)
    message = models.TextField()
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Contact Schools'

    def __str__(self):
        return self.name


class Personals(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='personals', blank=True)

    class Meta:
        verbose_name_plural = 'Personals'

    def __str__(self):
        return self.title


class SingleFeature(models.Model):
    personal = models.ForeignKey(Personals, on_delete=models.CASCADE)
    feature = models.CharField(max_length=230)

    class Meta:
        verbose_name_plural = 'Single Feature'

    def __str__(self):
        return self.feature


class SchoolTeacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    title = models.CharField(max_length=400, blank=True)
    image = models.ImageField(upload_to='school/teachers', blank=True)

    class Meta:
        verbose_name_plural = 'School Teachers'

    def __str__(self):
        return self.name


class SchoolInformation(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    mail = models.EmailField(unique=True, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'School Information'

    def __str__(self):
        return self.mail

class SocialLink(models.Model):
    school_info = models.ForeignKey(SchoolInformation, on_delete=models.CASCADE)
    social_urls = models.CharField(max_length=400)
    social_class = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Social Links'

    def __str__(self):
        return self.social_class


class SchoolNews(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to='school/news', blank=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'School News'

    def __str__(self):
        return self.title


def post_save_receiver(instance, created, sender, **kwargs):
    if created:
        s = SchoolHomePage.objects.create(school=instance)
        c = SchoolAchievement.objects.create(school=instance)
        h = SchoolNews.objects.create(school=instance)
        oo = SchoolInformation.objects.create(school=instance)
        l = SchoolService.objects.create(school=instance)
        sc = SchoolTeacher.objects.create(school=instance)
        ho = SchoolTestimonial.objects.create(school=instance)
        ot = Personals.objects.create(school=instance)
        ab = AboutSchool.objects.create(schoool=instance)


post_save.connect(post_save_receiver, sender=School)
