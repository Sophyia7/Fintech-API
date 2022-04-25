from email import message
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from accounts.models import User
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class DepositView(GenericAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = get_object_or_404(User, pk=request.user.pk)
            serializer.validated_data["user"] = user
            transaction_type = serializer.validated_data.get("type")
            
            if transaction_type == "deposit":
                    serializer.save()  
                    
                    return Response(
                        {
                        "message": "Deposit successfully",
                        "data": serializer.data
                        },
                        status=status.HTTP_200_OK
                    )
            else:
                return Response(
                    {
                        "message": "Error occured while deposting funds. Select the right type of transaction you make.",
                        "data": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            
class WithdrawView(GenericAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = get_object_or_404(User, pk=request.user.pk)
            serializer.validated_data["user"] = user
            transaction_type = serializer.validated_data.get("type")

            if transaction_type == "withdraw":
                serializer.save()  
            
                        
                return Response(
                    {
                        "message": "Withdrawl successfully",
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "message": "Error occured while withdrawing funds. Select the right type of transaction you want to make.",
                        "data": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
class GetTransactions(GenericAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        transactions = Transaction.objects.filter(user=user)
        serializer = self.serializer_class(instance=transactions, many=True)
        
        return Response(
            {
                "message": "Your transactions are below",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
        

                 