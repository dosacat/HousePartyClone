from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse;
from rest_framework import generics;
from .serializers import RoomSerializer;
from .models import Room
import json

# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
