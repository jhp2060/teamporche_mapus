from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from building_map.serializers import FloorSerializer, BuildingSerializer, FacilitySerializer
from .models import Floor, Facility, Building

class BuildingDetailView(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer



class FloorDetailView(generics.RetrieveAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class BuildingFloorDetailView(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get(self, request, *args, **kwargs):
        # automatically get pk from url
        floor_number = kwargs.get('floor_number')
        if floor_number is None:
            return Response(data={'error': 'url invalid'},
                            status=status.HTTP_404_NOT_FOUND)
        # queryset = self.get_queryset()
        building = self.get_object()
        floor = building.floors.get(number=floor_number)
        fs = FloorSerializer(floor)
        # if fs.is_valid(raise_exception=True):
        #   fs.validated_data
        # else :
        #   fs.errors
        return Response(fs.data, status=status.HTTP_200_OK)

class BuildingFloorFacilityListView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get(self, request, *args, **kwargs):
        floor_number = kwargs.get('floor_number')
        facility_type = kwargs.get('facility_type')
        if floor_number is None or facility_type is None:
            return Response(data={'error': 'url invalid'},
                            status=status.HTTP_404_NOT_FOUND)
        building = self.get_object()
        floor = building.floors.get(number=floor_number)
        facilities = floor.facilities.get(type=facility_type)
        fs = FacilitySerializer(facilities)
        return Response(fs.data, status=status.HTTP_200_OK)


'''
class Test(generics.ListAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    def filter_queryset(self, queryset):

    def get(self, request, *args, **kwargs):
        params = request.data
        params['key']

        obj = self.get_object()
        serializer = self.get_serializer(obj, params)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
'''
