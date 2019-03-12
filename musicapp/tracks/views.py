from django.shortcuts import render, get_object_or_404
from .models import hiphopTracks,recordLabels

# Create your views here.
def gettracks(request):
    tracks_list=hiphopTracks.objects.all()
    return render(request,'tracks/hiphop.html', {'tracks_list' : tracks_list} )