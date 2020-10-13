from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # symmetrical=False : 자동 맞팔 금지
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')