from django.db import models


class Room(models.Model):
    name = models.CharField('name', max_length=50)
    is_available = models.BooleanField()
