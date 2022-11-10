from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from users.serializers import User
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


class UserView(APIView):
    def post(self, requst):
        serializer = UserSerializer(data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"massage" : "회원 가입이 완료되었습니다!"})
        

class CustomTokenObtainPairView(TokenObtainPairView):
        serializer_class = CustomTokenObtainPairSerializer