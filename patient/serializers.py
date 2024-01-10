from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)#user disi karon Patient model a user attribute ase, r many=False korsi karon OneToOne relationship ache , but one to many or ForeignKey relationship thakle ba manytomany thakle many=True kortam, bujso paglu
    class Meta:
        model = Patient
        fields = '__all__'