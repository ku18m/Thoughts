from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
import jwt
from datetime import datetime, timedelta, timezone

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first() or User.objects.filter(email=email).first()

        if user is None:
            return Response({'error': 'Invalid username or email'})

        if not user.check_password(password):
            return Response({'error': 'Invalid password'})

        response = Response()
        payload = {
            'id': str(user.id),
            'exp': datetime.now(tz=timezone.utc) + timedelta(minutes=60),
            'iat': datetime.now(tz=timezone.utc)
        }
        user = UserSerializer(user).data
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response.set_cookie(key='X-Token', value=token, httponly=True)
        response.data = user
        response.status_code = 200
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('X-Token')
        if not token:
            return Response({'error': 'Token is missing'}, status=401)
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token is expired'}, status=401)
        except jwt.InvalidTokenError:
            return Response({'error': 'Token is invalid'}, status=401)
        user = User.objects.get(id=payload['id'])
        user = UserSerializer(user).data
        return Response(user)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('X-Token')
        response.data = {'message': 'Success'}
        return response
