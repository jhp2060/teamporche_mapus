from django.shortcuts import render
from django.views import generic

from .models import Floor, Facility, Building


class BuildingDetailView(generic.DetailView):
    model = Building
    

class FloorDetailView(generic.DetailView):
    model = Floor
    context_object_name = 'floor'

class FloorListView(generic.ListView):
    model = Floor
    context_object_name = 'floor_list'


