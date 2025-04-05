from datetime import datetime
import uuid

from django.shortcuts import render
from django.views.generic import TemplateView

from shows.models import Show
from venues.models import Event, Venue, Seat, Room, BookedSeat
from .models import Order

from django.http import HttpResponse

class HomePageView(TemplateView):
	template_name = 'home.html'


def trending_page_view(request):
	context = {
		'shows': Show.objects.filter(public=1)
	}
	return render(request, 'trending.html', context)

def event_page_view(request, pk):
	event = Event.objects.get(pk=pk)
	room = Room.objects.get(pk=event.room_number)

	if request.method == "GET":
		seats = Seat.objects.filter(room_number=room.room_id)
		booked_seats = BookedSeat.objects.filter(event=event, booked_status=True)

		for booked_seat in booked_seats:
			for seat in seats:
				if seat.seat_number == booked.seat_number:
					booked_seat.booked = 'true'

		context = {
			'room': room,
			'seats': seats,
			'event': event,
		}
		return render(request, 'event.html', context)
	
	elif request.method == "POST":
		seats = request.POST.get('seats').split("-")
		
		# convert to objects and make additional checks
		for index in range(len(seats)):
			if request.user.is_premium:
				seats[index] = Seat.objects.get(
					# check if valid seat
					seat_number=seats[index], 
					room_number=room.room_id,
				)
			else:
				# remove premium seats if user is not premium
				seats[index] = Seat.objects.get(
					seat_number=seats[index], 
					room_number=room.room_id,
					seat_premium=False
				)

		total = float(len(seats) * event.price)
		
		# add stripe payment here

		# if payment is successful
		order_id = uuid.uuid4()

		order = Order.objects.create(
			order_id=order_id, 
			user=request.user,
			total=total
		)

		for seat in seats:
			BookedSeat.objects.create(
				booking_id=uuid.uuid4(),
				order=order,
				seat_number=seat,
				event=event,
			)

		return HttpResponse(str(seats) + str(total))


def venues_page_view(request):
	context = {
		'venues': Venue.objects.all()
	}
	return render(request, 'venues.html', context)