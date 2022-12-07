from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        EXECUTIVE = "EXECUTIVE", "executive"
        MANAGER = "MANAGER", "Manager"
        ARTIST = "ARTIST", "artist"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class ArtistManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ARTIST)


class Student(User):

    base_role = User.Role.ARTIST

    artist = ArtistManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for artists"


@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "ARTIST":
        ArtistProfile.objects.create(user=instance)


class ArtistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True, blank=True)


class ManagerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)


class Manager(User):

    base_role = User.Role.MANAGER

    teacher = ManagerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for managers"


class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Manager)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "MANAGER":
        ManagerProfile.objects.create(user=instance)