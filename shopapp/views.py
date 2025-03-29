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
	room = Room.objects.get(room_id=event.room_number)

	if request.method == "GET":
		# generate an empty 2d list of the grid
		grid = [[None for y in range(room.room_columns)] for x in range(room.room_rows)]

		seats = Seat.objects.filter(room_number=room.room_id)
		booked_seats = BookedSeat.objects.filter(event=event, booked_status=True)

		# populate with seat objects
		for seat in seats:
			grid[seat.location_row][seat.location_column] = {'seat': seat, 'booking': None}

		# populate with booked seat objects
		for booked in booked_seats:
			grid[booked.seat_number.location_row][booked.seat_number.location_column]['booking'] = booked

		context = {
			'event': event,
			'room': room,
			'grid': grid
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