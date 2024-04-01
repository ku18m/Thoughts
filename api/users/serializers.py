from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    """User serializer."""
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Called from .save() method in the view to create a new user."""
        # We don't have to hash it here because the password is hashed in the model.
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        """Called from .save() method in the view to update the user."""
        if validated_data.get('password'):
            # Hash the password before saving it.
            validated_data['password'] = make_password(validated_data.get('password'))
        return super().update(instance, validated_data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        """Customizes the token response payload."""
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        token['id'] = str(user.id) # Because the id is an instance of UUID.
        
        # In case we dicided to add first_name and last_name to the token payload.
        # token['first_name'] = user.first_name
        # token['last_name'] = user.last_name

        return token
