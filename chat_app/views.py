from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ChatUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import Users
from django.contrib.auth.hashers import check_password

# Create your views here.
class ChatSignupView(APIView):
    def post(self, request):

        serializer = ChatUserSerializer(data=request.data)
        try:
            if serializer.is_valid():
                new_chat_user = serializer.save()
                response = {
                    "message": "User created successfully.",
                    "user_id": new_chat_user.id,
                    "name": new_chat_user.name,
                    "email": new_chat_user.email,
                    "phone": new_chat_user.phone,
                }

                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response(
                {"error": "User already exists."}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ChatLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        received_password = request.data.get("password")

        try:
            user = Users.objects.only('id', 'name', 'phone', 'password').get(email=email)

            if check_password(received_password, user.password):
                response_object = {
                    "message": "login successful",
                    "user_id": user.id,
                    "full_name": user.name,
                    "phone": user.phone,
                    "created_at": user.created_at,
                }
                return Response(response_object, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Users.DoesNotExist:
            return Response({'error': 'user not found'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()
            return Response({'error': 'server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)