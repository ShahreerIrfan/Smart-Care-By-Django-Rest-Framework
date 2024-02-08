from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('list', views.DoctorViewSet)
router.register('specialization', views.SpcealizationViewSet)
router.register('available_time', views.AvailableTimeViewSet)
router.register('designation', views.DesignationViewSet)
router.register('review', views.ReviewViewSet)
urlpatterns = [
    path('', include(router.urls)),
]