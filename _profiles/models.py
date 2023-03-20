from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=300,blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='profile_photos/%Y/%m/%d/')

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.photo.path)

    class Meta:
        verbose_name_plural='Profiles'



class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    profile_status = models.CharField(max_length=240)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_profile)
    
    class Meta:
        verbose_name_plural='Profile Status'