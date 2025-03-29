from datetime import datetime
import uuid

from django.shortcuts import render
from django.views.generic import TemplateView

from shows.models import Show
from venues.models import Event, Venue, Seat, Room
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
		seats = Seat.objects.filter(room_number=room.room_id)
		rows_list = [x for x in range(room.room_rows)]
		columns_list = [x for x in range(room.room_columns)]
		context = {
			'event': event,
			'room': room,
			'seats': seats,
			'rows_list': rows_list,
			'columns_list': columns_list
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
		Order.objects.create(
			order_id=uuid.uuid4(), 
			user=request.user.id,
			total=total,
		)

		print(datetime.now().strftime("[%d/%b/%Y %H:%M:%S] ") + "Booking created")
		return HttpResponse(str(seats) + str(total))


def venues_page_view(request):
	context = {
		'venues': Venue.objects.all()
	}
	return render(request, 'venues.html', context)