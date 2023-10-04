from rest_framework import serializers
from kyc.models import KYC

class KYCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYC
        fields = [
          'id', 'user', 'kyc_type', 'kyc_number', 'kyc_image', 'kyc_status', 'kyc_date'
        ]
        read_only_fields = ['id', 'kyc_date']