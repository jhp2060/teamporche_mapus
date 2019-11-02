from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     university = models.ForeignKey(
#         'account.University',
#         on_delete=models.SET_NULL,
#         null=True,
#     )
#     friends = models.ManyToManyField(
#         'self',
#     )
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     school_year = models.IntegerField(
#         default=1,
#     )


class University(models.Model):
    name = models.CharField(
        max_length=200,
    )
    def __str__(self):
        return self.name




class Pin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

