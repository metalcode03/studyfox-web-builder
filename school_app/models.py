from django.core.checks import messages
from django.db import models
from django.db.models.fields import related
from django.shortcuts import reverse
from django_countries.fields import CountryField


class School(models.Model):
    name = models.CharField(max_length=40, blank=True)
    logo = models.ImageField(upload_to='profilio/logo', blank=True)
    description = models.TextField(blank=True)
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
    registered_students = models.PositiveIntegerField(blank=True)
    qualified_teachers = models.PositiveIntegerField(blank=True)
    graduated_students = models.PositiveIntegerField(blank=True)
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
    cvc = models.CharField(blank=True, unique=True, max_length=200)
    description = models.TextField(blank=True)

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
