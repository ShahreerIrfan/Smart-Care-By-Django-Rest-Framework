from rest_framework import serializers
from . import models

class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = '__all__'
