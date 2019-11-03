from django.shortcuts import render
from rest_framework import generics

from building_map.serializers import FloorSerializer, BuildingSerializer
from .models import Floor, Facility, Building


class FloorDetailView(generics.RetrieveAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class BuildingDetailView(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

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
