from rest_framework import serializers 
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
        input validations and saves 
    """
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'age', 'username', 'password', 'confirm_password']
    
    def validate(self, data):
        if not self.instance and not ('password' in data and 'confirm_password' in data):
            return serializers.ValidationError('Password needed for registration.')

        if 'password' in data and 'confirm_password' in data:
            if data['password'] != data['confirm_password']:
                return serializers.ValidationError('Passwords do not match')

        return data 
    
    def create(self, validated_data):

        password = validated_data.pop('password')
        validated_data.pop('confirm_password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        if user.pk: 
            Token.objects.create(user=user)
        return user 

    def update(self, instance, validated_data):

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
        instance.save()

        return instance 