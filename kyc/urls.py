# Django imports
from django.urls import path

# App imports
from kyc.views import KYCView, KYCStatusView

urlspattern = [
    path("kyc", KYCView.as_view(), name="kyc"),
    path("kyc-status", KYCStatusView.as_view(), name="kyc-status"),
]