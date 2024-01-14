from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)#user disi karon Patient model a user attribute ase, r many=False korsi karon OneToOne relationship ache , but one to many or ForeignKey relationship thakle ba manytomany thakle many=True kortam, bujso paglu
    class Meta:
        model = Patient
        fields = '__all__'
        

#patient er registration form toiri
class RegistrationSerializerPatient(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)#ekhane confirm_password field dite hobe
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        
    # save method use korte hobe validation check korar jonno o save korar jonno
    def save(self):
        username = self.validated_data['username'] # serializer er khetre cleaned_data er poriborte validated_data use korte hobe
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        # upore sob data pailam r vaiable/attribute er modhe save korlam
        # ebar validation check korbo
        
        #password check
        if password != password2:
            raise serializers.ValidationError({'error': "Oops, Your password didn't match!"})
        
        #email check
        if User.objects.filter(email=email).exists():# jodi User modhe register form a dewa email exist kore
            raise serializers.ValidationError({'error': "Email already exists!"})
        
        #databse a data save korbo
        account = User(username=username, email=email, first_name=first_name, last_name=last_name)
        #print(account)
        #password save korbo ebar account a set_password method die
        account.set_password(password)
        account.is_active = False
        account.save() # account ta save korlam
        return account
    
    
# model form jevabe use kortam, same, ekhane forms.Form use kora hoise, upore sob forms.Modelform use kora hoise, same to same
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
        
        
            