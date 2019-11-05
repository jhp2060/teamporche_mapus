from rest_framework import serializers
from .models import Facility, Floor, Building


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    # nested serializer : 실존하는 필드명만 사용할 것
    # facilities = serializers.SerializerMethodField()
    # map_image = serializers.ImageField(use_url=True)

    class Meta:
        model = Floor
        fields = '__all__'

    # def get_facilities(self, instance):
    #     sorted_facilities = instance.facilities.all().order_by('type')
    #     return FacilitySerializer(sorted_facilities, many=True).data



class SimpleFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('pk', 'number')


class BuildingSerializer(serializers.ModelSerializer):
    floors = SimpleFloorSerializer(many=True)

    class Meta:
        model = Building
        fields = '__all__'


class SimpleBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('pk', 'name')
