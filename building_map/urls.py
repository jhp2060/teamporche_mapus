from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'building_map'

router = routers.DefaultRouter()
router.register('facilities', FacilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
