from django.shortcuts import render
from rest_framework import viewsets
from django.urls import path,include
from . import models
from . import serializer
# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.ContacUs.objects.all()
    serializer_class = serializer.ContactUsSerializer

