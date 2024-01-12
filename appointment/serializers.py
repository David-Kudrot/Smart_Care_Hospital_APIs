from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField(many=False) # many=False cuz, in models.py we used ForeignKey relationship
    doctor = serializers.StringRelatedField(many=False) # many=False cuz, in models.py we used ForeignKey relationship
    time = serializers.StringRelatedField(many=False)
    class Meta:
        model = Appointment
        fields = '__all__'