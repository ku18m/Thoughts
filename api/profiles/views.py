from django.shortcuts import render
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class Viewprofile(APIView):
    def get(self, request):
        return Response(Profile.objects.all().first().user.username)