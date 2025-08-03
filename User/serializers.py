from rest_framework import serializers
from .models import User, Account
from django.contrib.auth import authenticate
from Notifications.serializers import NotificationSerializer
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value
    
class user_serializer(serializers.ModelSerializer) :
    notifications = NotificationSerializer(many=True, read_only=True)

    class Meta :
        model  = User
        fields = ['username', 'email', 'role','notifications']
        read_only_fields = ['notifications']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(
            **validated_data,
            password=password
        )
        return user

class accounts_serializer(serializers.ModelSerializer) :
    username = serializers.CharField(source='user.username')
    email    = serializers.CharField(source='user.email')
    class Meta :
        model = Account
        exclude = ['id', 'created_at', 'user']
        read_only_fields = ['id','user','username','email']
