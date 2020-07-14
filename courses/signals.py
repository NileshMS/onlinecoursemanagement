from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from courses.models import ProfileModel

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(User=instance)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    instance.profilemodel.save()