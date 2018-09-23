from django.db import models


class Room(models.Model):
    name = models.CharField('name', max_length=50)
    is_available = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.name)


class Meeting(models.Model):
    description = models.CharField('description', max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_at = models.DateTimeField('start_at')
    end_at = models.DateTimeField('end_at')

    def __str__(self):
        return '{}'.format(self.description)
