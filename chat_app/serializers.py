from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password

class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

    def create(self, validated_data):
        plain_text_password = validated_data['password']
        hashed_password = make_password(plain_text_password)
        validated_data['password'] = hashed_password
        return super().create(validated_data)
