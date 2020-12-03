# Generated by Django 2.2.11 on 2020-12-03 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_app', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.CharField(max_length=15, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_app.School')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.CharField(blank=True, max_length=20, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school_app.School')),
                ('students', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
            options={
                'verbose_name': 'Students',
                'verbose_name_plural': 'Students',
            },
        ),
    ]
