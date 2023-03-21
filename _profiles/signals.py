from django.contrib.auth.models import User
from _profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(instance.username, '___Created___:',created)
    if created:
        Profile.objects.create(user=instance)


'''
Django yukarıdaki işlemleri ne zaman ve nasıl çalıştıracağını bilmiyor.
'''

