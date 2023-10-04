# Django imports
from django.shortcuts import get_object_or_404

# App imports
from kyc.serializers import KYCSerializer
from kyc.models import KYC
from accounts.models import User

# rest_framework imports
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class KYCView(GenericAPIView):
  serializer_class = KYCSerializer
  permission_classes = (IsAuthenticated)

  def post(self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      user = get_object_or_404(User, pk=request.user.id)
      serializer.validated_data['user'] = user
      serializer.save(user=user)

      return Response(
        {"message": "KYC submitted successfully"},
        status=status.HTTP_201_CREATED
      )

class KYCStatusView(GenericAPIView):
  serializer_class = KYCSerializer
  permission_classes = (IsAuthenticated)

  def get(self, request, pk):
    kyc = get_object_or_404(KYC, pk=pk)
    serializer = self.serializer_class(kyc)
    kyc_status = serializer.data['kyc_status'] 

    if kyc_status == "True":
      return Response(
        {"message": "KYC is approved"},
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {"message": "KYC is not approved, reupload your KYC"},
        status=status.HTTP_200_OK
      )




