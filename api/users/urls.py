from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('auth/', UserView.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
