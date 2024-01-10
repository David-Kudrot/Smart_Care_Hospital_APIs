from rest_framework import serializers
from .models import Specialization, Designation, AvailableTime, Doctor, Review


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'
        
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
        
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'
        
class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)# many=False karon OneToOne relationship
    specialization = serializers.StringRelatedField(many=True)#many=True karon many to many relationship
    designation = serializers.StringRelatedField(many=True) # many=True karon many to many relationship
    available_time = serializers.StringRelatedField(many=True)#many=True karon many to many relationship
    class Meta:
        model = Doctor
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'