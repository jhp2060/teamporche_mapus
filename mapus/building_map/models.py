from django.contrib.auth import get_user_model
from django.db import models

from account.models import Pin
from campus_map.models import Campus

User = get_user_model()

class Building(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="건물명",
    )
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
    )
    upper_latitude = models.FloatField()
    lower_latitude = models.FloatField()
    left_longtitude = models.FloatField()
    right_longtitude = models.FloatField()
    def __str__(self):
        return self.campus.university.name + " " + self.name

class Floor (models.Model):
    number = models.IntegerField()
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
    )
    map_img = models.ImageField()

    def __str__(self):
        return self.building.campus.university.name \
               + " " + self.building.name \
               + " " + str(self.number) + "층"

class Facility (Pin):
    type = models.CharField(
        max_length=200,
        verbose_name="편의시설유형",
    )
    description = models.TextField(
        max_length=1000,
    )
    registered_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        #on_delete=models.SET_DEFAULT,
        # default=
    )
