from django.shortcuts import render

from rest_framework import viewsets
from django.urls import path,include
from . import models
from . import serializer
# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializer.ServiceUsSerializer
