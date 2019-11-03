from rest_framework import serializers
from .models import Facility, Floor, Building


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    # nested serializer : 실존하는 필드명만 사용할 것
    facilities = FacilitySerializer(many=True)
    map_image = serializers.ImageField(use_url=True)
    class Meta:
        model = Floor
        fields = '__all__'


class SimpleFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('pk', 'number')


class BuildingSerializer(serializers.ModelSerializer):
    floors = SimpleFloorSerializer(many=True)
    class Meta:
        model = Building
        fields = '__all__'
