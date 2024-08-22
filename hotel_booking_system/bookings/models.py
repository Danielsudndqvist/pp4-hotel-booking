from django.db import models

# Create your models here.

from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    amenities = models.TextField()
    image = models.ImageField(upload_to='hotels/')
    # More fields as needed

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return f'{self.room_type} - {self.hotel.name}'