from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'building_map'

urlpatterns = [
    path('building/<int:pk>/', BuildingDetailView.as_view(),
         name='building_detail'),

    path('floor/<int:pk>/', FloorDetailView.as_view(),
         name='floor_detail'),

]
