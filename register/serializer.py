from django.forms import ValidationError
from rest_framework import serializers
from register.models import RegisterUser as User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','is_jobsekeer','is_jobposter']
    
    def validate(self, attrs):
        is_jobsekeer = attrs.get('is_jobsekeer')
        is_jobposter = attrs.get('is_jobposter')
        if is_jobsekeer==is_jobposter:
            raise ValidationError("only can one choice job sekeer or job poster")
        
        return attrs

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']