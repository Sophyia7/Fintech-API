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
            transaction_type = serializer.validated_data.get("transaction_type")
            amount = serializer.validated_data.get("amount")
            user_wallet = Wallet.objects.get(user=user)
            # status = serializer.validated_data.get("status")
            
            if transaction_type == "deposit":
                user_wallet.available_amount += amount
                user_wallet.save()
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
            transaction_type = serializer.validated_data.get("transaction_type")
            amount = serializer.validated_data.get("amount")
            user_wallet = Wallet.objects.get(user=user)


            if transaction_type == "withdraw":
                if amount > user_wallet.available_amount:
                    return Response(
                        {
                            "message": "Insufficient funds"
                        },
                        status=status.HTTP_200_OK
                    )
                else:
                    user_wallet.available_amount -= float(amount)
                    user_wallet.save()
                    serializer.save()
     
                return Response(
                    {
                        "message": "Withdrawal successfully",
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
        


class GetWallet(GenericAPIView):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        user = get_object_or_404(User, pk=request.user.id)
        balance = Wallet.objects.filter(user=user)
        serializer = self.serializer_class(instance=balance, many=True)
        
        return Response(
            {
                "message": "Balance retrieved",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )            


class GetDepositStatus(GenericAPIView):
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        transaction_status = Transaction.objects.filter(user=user, transaction_type="deposit")
        current_status = transaction_status.last().status
        serializer = self.serializer_class(instance=transaction_status, many=True)

        if current_status == "pending":
            return Response(
                {
                    "message": "Your deposit is pending",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        elif current_status == "processing":
            return Response(
                {
                    "message": "Your deposit is processing",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        elif current_status == "processed":
            return Response(
                {
                    "message": "Your deposit is completed",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "message": "You have no transaction records yet"
                },
                status=status.HTTP_200_OK
            )



class GetWithdrawStatus(GenericAPIView):
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        transaction_status = Transaction.objects.filter(user=user, transaction_type="withdraw")
        current_status = transaction_status.last().status
        serializer = self.serializer_class(instance=transaction_status, many=True)

        if current_status == "pending":
            return Response(
                {
                    "message": "Your withdrawal is pending",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        elif current_status == "processing":
            return Response(
                {
                    "message": "Your withdrawal is processing",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        elif current_status == "processed":
            return Response(
                {
                    "message": "Your withdrawal is completed",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "message": "You have no transaction records yet"
                },
                status=status.HTTP_200_OK
            )
