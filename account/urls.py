from django.contrib import admin
from django.urls import path, include

from account.views import UniversityDetailView

app_name = 'account'

urlpatterns = [
    #path('login/', , namespace='login'),
    path('university/<int:pk>/', UniversityDetailView.as_view()),
]
