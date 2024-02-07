from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointModelAdmin(admin.ModelAdmin):
    list_display =['patinet_Name','doctor_Name','appointment_Type','appointment_Stutas','synptom','time','cancel']
    def patinet_Name(self,obj):
        return obj.patient.user.first_name
    def doctor_Name(self,obj):
        return obj.doctor.user.last_name
    
admin.site.register(Appointment,AppointModelAdmin)