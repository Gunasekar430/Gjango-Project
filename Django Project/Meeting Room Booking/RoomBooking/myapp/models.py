from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField( max_length=50)
    capacity = models.IntegerField(default=5)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.room_name


class Meeting(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    start_Time = models.TimeField( auto_now=True, auto_now_add=False)
    end_Time = models.TimeField( auto_now=False, auto_now_add=False)
    booked_by = models.CharField( max_length=50)

    def __str__(self):
        return self.title