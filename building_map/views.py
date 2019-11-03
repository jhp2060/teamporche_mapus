from django.shortcuts import render
from rest_framework import generics, viewsets

from building_map.serializers import FloorSerializer, FacilitySerializer
from .models import Floor, Facility, Building

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

'''
class Test(generics.ListAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    def filter_queryset(self, queryset):

    def get(self, request, *args, **kwargs):
        params = request.data
        params['key']

        obj = self.get_object()
        serializer = self.get_serializer()
        serializer(obj, params)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
'''
