from django.shortcuts import render
from .serializers import AppointmentSerializer
from .models import Appointment
from rest_framework import viewsets
# Create your views here.

class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    # custom query parameters url a pass korle sei parameter k set korte ekhane get_queryset method use korte hobe, mane url a jodi patient_id=1 parameter pass korte chai tobe ekhane sei patient_id param ta set korte ei method use korbo
    
    def get_queryset(self):
        queryset = super().get_queryset() 
        patient_id = self.request.query_params.get('patient_id')# url theke parameter ta get korlam
        
        # ebar check korbo je jodi patient_id exist kore
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)#present_attribute_patient_id = patient_id_from_url
        return queryset
