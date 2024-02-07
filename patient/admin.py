from django.contrib import admin
from .models import Patient
# Register your models here.
class PatientModelAdmin(admin.ModelAdmin):
    list_display =['First_Name','Last_Name','mobile_no','image']
    def First_Name(self,obj):
        return obj.user.first_name
    def Last_Name(self,obj):
        return obj.user.last_name
    

admin.site.register(Patient,PatientModelAdmin)