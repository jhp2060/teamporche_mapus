from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
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
        related_name='floors',
    )
    map_image = models.ImageField(
        upload_to='media/building_map/',
        default='default_map.png'

    )

    class Meta:
        ordering=["number"]
        verbose_name_plural="Floors"

    def __str__(self):
        return self.building.university.name \
               + " University : floor " + str(self.number) \
               + " of " + self.building.name


class Facility(models.Model):
    TYPE_CHOICES = (
        ('JS', '정수기'),
        ('IS', '인쇄기'),
        ('SH', '소화기'),
        ('HJ', '화장실'),
        ('SM', '수면실'),
        ('SS', '샤워실'),
    )
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=None,
    )
    floor = models.ForeignKey(
        Floor,
        on_delete=models.CASCADE,
        default=None,
        related_name='facilities',
    )
    latitude = models.FloatField(
        # validators = [MinValueValidator(floor.building.upper_latitude),
        #               MaxValueValidator(floor.building.lower_latitude)],
    )
    longitude = models.FloatField(
        # validators = [MinValueValidator(floor.building.left_longitude),
        #               MaxValueValidator(floor.building.right_longitude)],
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
    )
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name_plural="Facilities"

    def __str__(self):
        return "facility " + str(self.pk) + " : " + self.type \
               + " at floor " +  str(self.floor.number) \
               + " " + self.floor.building.name