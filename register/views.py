from ast import Return
from rest_framework import generics as gn 
from register.serializer import RegisterSerializer,UserLoginSerializer
from register.models import RegisterUser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate,login,logout

class RegisterAPI(gn.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    queryset = RegisterUser
    def set_password(self,email,password):
        obj = RegisterUser.objects.get(email=email)
        obj.set_password(password)
        obj.save()

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']
        user = super().post(request, *args, **kwargs)
        self.set_password(email,password)
        return Response({"status":"success","message":"user register","user":email})
    
class LoginAPI(gn.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    queryset = RegisterUser

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request,email=email,password=password)
        if user is None:
            return Response({"status":"failed",'message':"failed to login"})
        else:
            return Response({"status":"success",'message':"you login successfully"})
    