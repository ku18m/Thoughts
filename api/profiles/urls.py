from django.urls import path, include
from .views import Viewprofile

urlpatterns = [
    path('profiles/', Viewprofile.as_view(), name='profile'),
]
