# Generated by Django 4.1.7 on 2023-03-21 14:42

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=300, null=True)),
                ('city', models.CharField(blank=True, max_length=80, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='ProfileStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_status', models.CharField(max_length=240)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_profiles.profile')),
            ],
            options={
                'verbose_name_plural': 'Profile Status',
            },
        ),
    ]
