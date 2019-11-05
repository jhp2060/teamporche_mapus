from django.contrib.auth import get_user_model
from rest_framework import serializers

from account.models import University
from building_map.serializers import SimpleBuildingSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()


class UniversitySerializer(serializers.ModelSerializer):
    buildings = SimpleBuildingSerializer(many=True)
    class Meta:
        model = University
        fields = '__all__'





