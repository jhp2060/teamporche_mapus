from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    university = models.ForeignKey(
        'account.University',
        on_delete=models.SET_NULL,
        null=True,
        default=None,
    )
    friends = models.ManyToManyField(
        'self',
        default=None,
    )
    latitude = models.FloatField(default=-1)
    longitude = models.FloatField(default=-1)
    school_year = models.IntegerField(default=-1)
    class Meta:
        ordering=["username"]
        verbose_name_plural="Users"


class University(models.Model):
    name = models.CharField(
        max_length=200,
    )
    def __str__(self):
        return self.name
    class Meta:
        ordering=["name"]
        verbose_name_plural="Universities"
