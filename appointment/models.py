from django.db import models
from patient.models import Patient
from doctor.models import AvailableTime, Doctor

# Create your models here.
APPOINTMENT_TYPES = (
    ('Online', 'Online'),
    ('Offline', 'Offline'),
)
APPOINTMENT_STATUS = (
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
)
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_status = models.CharField(max_length=50, choices=APPOINTMENT_STATUS, default="Pending")
    appointment_types = models.CharField(max_length=50, choices=APPOINTMENT_TYPES)
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE, null=True)
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name}, Patient: {self.patient.user.first_name}"
    
    
    
    
    