from django.conf.urls import url
from django.contrib import admin

from .views import (
    LogInView, ResendActivationCodeView, RemindUsernameView, SignUpView, ActivateView, LogOutView,
    ChangeEmailView, ChangeEmailActivateView, ChangeProfileView, ChangePasswordView,
    RestorePasswordView, RestorePasswordDoneView, RestorePasswordConfirmView,
)

app_name = 'accounts'

urlpatterns = [
    url('log-in/', LogInView.as_view(), name='log_in'),
    url('log-out/', LogOutView.as_view(), name='log_out'),

    url('resend/activation-code/', ResendActivationCodeView.as_view(), name='resend_activation_code'),

    url('sign-up/', SignUpView.as_view(), name='sign_up'),
    url('activate/<code>/', ActivateView.as_view(), name='activate'),

    url('restore/password/', RestorePasswordView.as_view(), name='restore_password'),
    url('restore/password/done/', RestorePasswordDoneView.as_view(), name='restore_password_done'),
    url('restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(), name='restore_password_confirm'),

    url('remind/username/', RemindUsernameView.as_view(), name='remind_username'),

    url('change/profile/', ChangeProfileView.as_view(), name='change_profile'),
    url('change/password/', ChangePasswordView.as_view(), name='change_password'),
    url('change/email/', ChangeEmailView.as_view(), name='change_email'),
    url('change/email/<code>/', ChangeEmailActivateView.as_view(), name='change_email_activation'),
]
