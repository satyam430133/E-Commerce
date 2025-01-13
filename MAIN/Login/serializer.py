from rest_framework import serializers
from .models import UserModel

class LoginSerializer(serializers.Serializer):
    class Meta():
        model   = UserModel
        fields  = "all"