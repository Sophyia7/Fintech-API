from django.urls import path
from .views import Register, Login, ResendActivationLink, ResetPassword, ActivateEmail, ConfirmPassword, Logout

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login user'),
    path('confirm-email/<str:user_id>/<str:token>', ActivateEmail.as_view(), name='activate email'),
    path('resend-activation-link/<str:email>', ResendActivationLink.as_view(), name='resend-activation-link'),
    path('reset-password/<str:email>', ResetPassword.as_view(), name='reset-password-token'),
    path("reset-password-confirm/<str:user_id>/<str:token>", ConfirmPassword.as_view(), name='confirm-password'),
    path('logout', Logout.as_view(), name='logout')
]