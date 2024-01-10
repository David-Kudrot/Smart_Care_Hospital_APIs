from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
# Create your views here.

class PatientViewSets(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
