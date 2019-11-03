from rest_framework import serializers
from .models import Facility, Floor


class FloorSerializer(serializers.ModelSerializer):
    facilities = serializers.PrimaryKeyRelatedField(many=True, queryset=Facility.objects.all())
    class Meta:
        model = Floor
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    #type_name = serializers.CharField(max_length=200,allow_blank=False)
    #floor_number = serializers.IntegerField(source='floor.number')
    class Meta:
        model = Facility
        fields = '__all__'



