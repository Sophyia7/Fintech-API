# rest_framework imports
from rest_framework import serializers

# App imports
from transactions.models import Transaction, Wallet

        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_type', 'amount', 'status', 'date_created']
        
        
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'available_amount', 'date_modified']
        
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'status']

class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount']