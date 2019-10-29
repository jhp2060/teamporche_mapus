from django.db import models
from django.contrib.auth.models import AbstractUser
from campus_map.models import Campus

class User(AbstractUser):
    university = models.OneToOneField(

    )
    friends = models.ManyToManyField(
        'self',
    )
    latitude = models.FloatField()
    longtitude = models.FloatField()

class University(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="대학교"
    )
    campus = models.OneToOneField(
        Campus,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name

class Pin(models.Model):
    latitude = models.FloatField()
    longtitude = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

