from django.db import models
from django.conf import settings

# Create your models here.
class Reservation(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    personnel = models.IntegerField()
    room_number = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=100)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
