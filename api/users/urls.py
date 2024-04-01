from django.urls import path, include
from .views import RegisterView, GetEmailView, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('modify', UserView.as_view(), name='handle_user'),
    path('register', RegisterView.as_view(), name='register'),
    path('token/get', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('get_email', GetEmailView.as_view(), name='get_username'),
]
