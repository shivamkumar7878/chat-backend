from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password

class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

    def validate(self, attrs):
        # checking if email is unique across all users
        received_email = attrs.get('email', None)
        is_email_unique = Users.objects.filter(email=received_email).exists()
        print("is_email_unique" , is_email_unique)
        if received_email and is_email_unique:
            raise serializers.ValidationError({"email": "User with this email already exists."})
        return attrs
    
    def create(self, validated_data):
        plain_text_password = validated_data['password']
        hashed_password = make_password(plain_text_password)
        validated_data['password'] = hashed_password
        return super().create(validated_data)
