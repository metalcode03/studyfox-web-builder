# Generated by Django 2.2.11 on 2021-01-10 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('class_app', '0001_initial'),
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('klass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='select_class', to='class_app.Class')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('school', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_app.School')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='class_app.Subject')),
            ],
            options={
                'verbose_name': 'Workers',
                'verbose_name_plural': 'Workers',
            },
        ),
    ]