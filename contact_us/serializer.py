from rest_framework import serializers
from . import models

class ContactUsSerializer(serializers.ModelSerializer):
    class meta:
        model = models.ContacUs
        fields = '__all__'
        