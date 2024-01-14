from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Patient
from . import serializers
from .serializers import PatientSerializer, RegistrationSerializerPatient, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
#for email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.views import View


# Create your views here.

class PatientViewSets(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    


# APIView for user registration
class UserRegistrationAPIView(APIView):
    serializer_class = RegistrationSerializerPatient
    
    #post request korbo get noi karon form submit kora hobe
    def post(self, request):
        serializer = self.serializer_class(data=request.data)#data instacne set kora holo data serializer class a built in keyword thake
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user) # ei specific user er jonno token generate kora holo
            
            uid = urlsafe_base64_encode(force_bytes(user.pk)) # user er pk die specific uid make kora hobe ja encode a convert hobe
            # user er jonno confirm_like make kora
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            
            # email send to user
            email_subject = "Confirm your email"
            email_body = render_to_string('confirm_email.html', {'confirm_link':confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            
            return Response("Check your mail for confirmation!")
        return Response(serializer.errors)
    
    
# function based activate account and check below has class based view

# def activate(request, uid64, token):
#     try:
#         uid = urlsafe_base64_decode(uid64).decode()
#         user = User._default_manager.get(pk=uid)
#     except(User.DoesNotExist):
#         user = None 
    
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return redirect('login')
#     else:
#         return redirect('register')
    
class ActivateAccount(View):
    def get(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64).decode()
            user = User._default_manager.get(pk=uid)
        except User.DoesNotExist:
            user = None 

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return redirect('register')
        

class UserLoginAPIView(APIView):
    def post(self, request):  # jehetu login korte form post kora lage tai only post use korlam
        serializer = UserLoginSerializer(data=self.request.data) # same to same jemon form = forms.UserLoginForm(user=self.request.user) kortam
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            
            user = authenticate(username=username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)# token = token thakbe or  _ = toaken create hobe
                print(token)
                print(_)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid Credentials!'})
        return Response(serializer.errors)
    
    
class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete() # toiri kora token ta delete kora holo jeno logout korar por same token die login na korte pare
        logout(request)
        return redirect('login')
        