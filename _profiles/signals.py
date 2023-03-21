from django.contrib.auth.models import User
from _profiles.models import Profile, ProfileStatus
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # print(instance.username, '___Created___:',created)
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_profile_status_message(sender, instance, created, **kwargs):
    
    if created:
        ProfileStatus.objects.create(
            user_profile = instance,
            profile_status = f'Merhaba benim kullanıcı adım:{instance.user.username}'
        )


'''
Django yukarıdaki işlemleri ne zaman ve nasıl çalıştıracağını bilmiyor.
'''

