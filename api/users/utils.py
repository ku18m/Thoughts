"""Utils functions for users app."""
from .models import User
from random import randint

def username_generator(email: str) -> str:
    """Generate a username from an email address."""
    email_prefix = email.split('@')[0].lower()
    while User.objects.filter(username=email_prefix).exists():
        email_prefix += str(randint(0, 9))
    return email_prefix
