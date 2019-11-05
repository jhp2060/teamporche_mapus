from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'building_map'

urlpatterns = [
    path('floor/<int:pk>/', FloorDetailView.as_view()),
    path('building/<int:pk>/floor/<int:floor_number>', BuildingFloorDetailView.as_view()),
    path('building/<int:pk>/floor/<int:floor_number>/facility/<str:facility_type>', BuildingFloorFacilityListView.as_view()),
]
