from django.contrib.auth import get_user_model
from django.db import models

from account.models import Pin

#User = get_user_model()

class Building(models.Model):
    name = models.CharField(
        max_length=200,
    )
    campus = models.ForeignKey(
        'campus_map.Campus',
        on_delete=models.CASCADE,
    )
    upper_latitude = models.FloatField()
    lower_latitude = models.FloatField()
    left_longitude = models.FloatField()
    right_longitude = models.FloatField()
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
    )
    floor = models.ForeignKey(
        Floor,
        on_delete=models.CASCADE,
        default=None,
    )
    description = models.TextField(
        max_length=1000,
    )