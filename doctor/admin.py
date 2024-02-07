from django.contrib import admin
from .models import Doctor,Spcealization,AvailableTime,Designation

# Register your models here.
# class DoctorModelAdmin(admin.ModelAdmin):
#     list_display = ['First_name','Last_Name']

#     def First_Name(self,obj):
#         return obj.user.first_name
#     def Lase_Name(self,obj):
#         return obj.user.last_name

admin.site.register(AvailableTime)

class SpcealizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}


admin.site.register(Spcealization,SpcealizationAdmin)
admin.site.register(Designation,DesignationAdmin)
admin.site.register(Doctor)
 