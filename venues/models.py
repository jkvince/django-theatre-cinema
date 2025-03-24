from django.db import models
import uuid

class Venue(models.Model):
    venue_id = models.SlugField(
        primary_key=True
    )
    venue_name = models.CharField()
    venue_address = models.CharField()
    venue_accessibility = models.BooleanField()
    working_hours = models.CharField()
    venue_latitude = models.FloatField()
    venue_longitude = models.FloatField()
    venue_contact = models.EmailField()


class Room(models.Model):
    room_number = models.CharField(
        primary_key=True
    )
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE)
    seat_layout = models.FileField()

    class Meta:
        unique_together = ('room_number', 'venue_id')


class Seat(models.Model):
    seat_number = models.CharField(
        primary_key=True
    )
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)

    seat_premium = models.BooleanField()
    seat_accessible = models.BooleanField()
    seat_price = models.FloatField()

    class Meta:
        unique_together = ('seat_number', 'room_number')
    

class BookedSeat(models.Model):
    booking_id = models.UUIDField(
        primary_key=True
    )
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    seat_number = models.ForeignKey(Seat, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    booked_status = models.BooleanField()
