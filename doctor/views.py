from django.shortcuts import render
from rest_framework import viewsets
from django.urls import path,include
from . import models
from . import serializer
# Create your views here.
    
class SpcealizationViewSet(viewsets.ModelViewSet):
    queryset = models.Spcealization.objects.all()
    serializer_class = serializer.SpcealizationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializer.DesignationSerializer

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializer.AvailableTimeSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializer.DoctorSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializer.ReviewSerializer
