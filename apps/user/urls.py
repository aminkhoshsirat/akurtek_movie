from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('manage-profile/', ManageProfileView.as_view(), name='manage_profile'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogOutView.as_view(), name='logout'),
    path('sign-up', SignUpView.as_view(), name='sign_up'),
    path('reset-password-send', ResetPasswordSendView.as_view(), name='reset_password_send'),
    path('reset-password/<code>', ResetPasswordView.as_view(), name='reset_password')
]