from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import * 
from .models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

# Create your views here.
class Register(GenericAPIView):
    serializer_class = UserSerailizer
    
    def post(self, request, format='json'):
        num_results = User.objects.filter(email=request.data["email"]).count()
        if num_results > 0:
            return Response(
                {
                    "message": "User already exists",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
                 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.is_active = True
            user.save()
            return Response(
            {
                "message":"User registered successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
        else:
            return Response(
                {
                    "message": "Error occured. Check the details entered.",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
class Login(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            return Response(
                {"message": "email or password is incorrect"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        current_password = user.password
        check = check_password(data["password"], current_password)

        if check:
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "message": "Login Successful",
                        "data": {
                            "user": {
                                "user_id": user.pk,
                                "email": user.email,
                            },
                            "refresh": str(refresh),
                            "access": str(refresh.access_token),
                        },
                    }
                )
        else:
            return Response(
                {
                    "message": "email or password is incorrect"
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )