from django.urls import path
from .views import *

urlpatterns =[
    path("deposit", DepositView.as_view(), name="deposit"),
    path("withdraw", WithdrawView.as_view(), name='withdraw'),
    path("transactions", GetTransactions.as_view(), name="transactions")
]