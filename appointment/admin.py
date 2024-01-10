from django.contrib import admin
from appointment.models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'patient_name', 'appointment_types', 'appointment_status', 'symptom', 'time', 'cancel']
    
    
    def doctor_name(self,obj):
        return f"{obj.doctor.user.first_name} {obj.doctor.user.last_name}"
    def patient_name(self,obj):
        return f"{obj.doctor.user.first_name} {obj.doctor.user.last_name}"
    
    
admin.site.register(Appointment, AppointmentAdmin)
    