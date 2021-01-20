# Generated by Django 2.2.11 on 2021-01-14 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageHomeView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='school/hero_image/hero')),
                ('school_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.SchoolHomePage')),
            ],
        ),
    ]