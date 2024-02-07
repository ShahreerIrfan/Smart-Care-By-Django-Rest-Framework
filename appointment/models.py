from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime
# Create your models here.
APPOINTMENT_STUTAS = [
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]
APPOINTMENT_TYPES = [
    ('Online','Online'),
    ('Offline','Offline'),
]
class Appointment(models.Model):
    patient =  models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_Type = models.CharField(choices=APPOINTMENT_TYPES,max_length=20)
    appointment_Stutas = models.CharField(choices=APPOINTMENT_STUTAS,max_length=20,default = "pending")
    synptom = models.TextField()
    time = models.ForeignKey(AvailableTime,on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)

    def __str__(self) -> str:
        return f"Doctor {self.doctor.user.first_name} Patient {self.patient.user.first_name}"

