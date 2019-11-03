from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Building(models.Model):
    name = models.CharField(max_length=100,blank=True,default='')
    university = models.ForeignKey(
        'account.University',
        on_delete=models.CASCADE,
        default=None,
    )
    upper_latitude = models.FloatField(default=0)
    lower_latitude = models.FloatField(default=0)
    left_longitude = models.FloatField(default=0)
    right_longitude = models.FloatField(default=0)

    class Meta:
        ordering=["name"]
        verbose_name_plural="Buildings"

    def __str__(self):
        return self.university.name + " " + self.name


class Floor(models.Model):
    number = models.IntegerField(default=0)
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
    )
    map_img = models.ImageField(
        blank=True,
    )

    class Meta:
        ordering=["number"]
        verbose_name_plural="Floors"

    def __str__(self):
        return self.building.university.name \
               + " University : floor " + str(self.number) \
               + " of " + self.building.name


class Facility(models.Model):
    type = models.CharField(
        max_length=200,
    )
    floor = models.ForeignKey(
        Floor,
        on_delete=models.CASCADE,
        default=None,
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        default=None,
        null=True,
    )
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name_plural="Facilities"
