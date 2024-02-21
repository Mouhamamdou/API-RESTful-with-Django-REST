from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'can_be_contacted', 'can_data_be_shared', 'created_time']
