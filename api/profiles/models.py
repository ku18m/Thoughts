from django.db import models
from common.models import BaseModel

# Create your models here.
class Profile(BaseModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
