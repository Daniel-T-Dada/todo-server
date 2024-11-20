from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        
        user = User(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    


    # def create(self, validated_data):
    #     print(validated_data)
    #     user = User(
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         username=validated_data['username'],
    #     )
    #     user.set_password(validated_data['password'])
    #     try:
    #         user.save()  # Save the user instance
    #     except Exception as e:
    #         raise serializers.ValidationError(
    #         {"error": str(e)})  # Raise validation error
    #     return UserSerializer(user).data


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'status', 'created_at', 'updated_at')
