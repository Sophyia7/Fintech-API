from django.urls import path
from .views import DepositView, TotalWithdraw,WithdrawView,GetTransactions,GetWallet,GetDepositStatus, GetWithdrawStatus, TotalDeposit, TotalWithdraw

urlpatterns =[
    path("deposit", DepositView.as_view(), name="deposit"),
    path("withdraw", WithdrawView.as_view(), name='withdraw'),
    path("transactions", GetTransactions.as_view(), name="transactions"),
    path("balance", GetWallet.as_view(), name="acc-balance"),
    path("deposit-status", GetDepositStatus.as_view(), name="deposit-status"),
    path("withdraw-status", GetWithdrawStatus.as_view(), name='withdraw-status'),
    path("total-deposit", TotalDeposit.as_view(), name='total-deposit'),
    path("total-withdraw", TotalWithdraw.as_view(), name='withdraw-deposit'),
]