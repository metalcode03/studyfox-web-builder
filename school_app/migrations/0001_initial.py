# Generated by Django 2.2.11 on 2020-12-03 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40)),
                ('logo', models.ImageField(blank=True, upload_to='profilio/logo')),
                ('description', models.TextField(blank=True)),
                ('school_founded', models.DateField(blank=True)),
                ('template_path', models.CharField(blank=True, max_length=30)),
                ('slug', models.SlugField(blank=True)),
                ('maintainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Schools',
                'verbose_name_plural': 'Schools',
            },
        ),
        migrations.CreateModel(
            name='SchoolTestimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='school/testimonial/image')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.School')),
            ],
            options={
                'verbose_name_plural': "School's Testimonials",
            },
        ),
        migrations.CreateModel(
            name='SchoolService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='school/service/image')),
                ('cvc', models.CharField(blank=True, max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.School')),
            ],
            options={
                'verbose_name_plural': 'School Service',
            },
        ),
        migrations.CreateModel(
            name='SchoolHomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_title', models.CharField(blank=True, max_length=40)),
                ('hero_text', models.TextField(blank=True)),
                ('hero_image', models.ImageField(blank=True, upload_to='school/hero_image')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.School')),
            ],
            options={
                'verbose_name_plural': 'School Home',
            },
        ),
        migrations.CreateModel(
            name='SchoolAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_students', models.PositiveIntegerField(blank=True)),
                ('qualified_teachers', models.PositiveIntegerField(blank=True)),
                ('graduated_students', models.PositiveIntegerField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.School')),
            ],
            options={
                'verbose_name_plural': "School's Achievements",
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='school/gallery/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.School')),
            ],
            options={
                'verbose_name_plural': 'Schools Gallery',
            },
        ),
        migrations.CreateModel(
            name='ContactSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('slug', models.SlugField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.School')),
            ],
            options={
                'verbose_name_plural': 'Contact Schools',
            },
        ),
        migrations.CreateModel(
            name='AboutSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, max_length=120)),
                ('image', models.ImageField(blank=True, upload_to='school/feature/image')),
                ('about', models.TextField(blank=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.School')),
            ],
            options={
                'verbose_name_plural': 'School About',
            },
        ),
    ]
