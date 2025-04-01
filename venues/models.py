from django.db import models
import uuid

from shows.models import Show
from shopapp.models import Order

class Venue(models.Model):
    venue_id = models.SlugField(
        primary_key=True
    )
    venue_name = models.CharField(
        max_length=30
    )
    venue_address = models.CharField(
        max_length=30
    )
    venue_accessibility = models.BooleanField()
    working_hours = models.CharField(
        max_length=10
    )
    venue_latitude = models.FloatField()
    venue_longitude = models.FloatField()
    venue_contact = models.EmailField(
        blank=True
    )

    def __str__(self):
        return self.venue_id


class Room(models.Model):
    room_id = models.SlugField(
        primary_key=True
    )
    room_number = models.CharField(
        max_length=15
    )
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE)
    room_rows = models.IntegerField()
    room_columns = models.IntegerField()

    class Meta:
        # Compound key
        unique_together = ('room_number', 'venue_id')

    def __str__(self):
        return self.room_id


class Seat(models.Model):
    seat_id = models.SlugField(
        primary_key=True
    )
    seat_number = models.CharField(
        max_length=10
    )
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)

    seat_premium = models.BooleanField()
    seat_accessible = models.BooleanField()
    location_row = models.IntegerField(default=1)
    location_column = models.IntegerField(default=1)

    class Meta:
        # Compound key
        unique_together = ('seat_number', 'room_number')


class Event(models.Model):
    event_id = models.IntegerField(
        primary_key=True
    )
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    event_time = models.DateTimeField()
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    price = models.FloatField()

class BookedSeat(models.Model):
    booking_id = models.UUIDField(
        primary_key=True
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    seat_number = models.ForeignKey(Seat, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booked_status = models.BooleanField(default=True)
