from datetime import datetime
import uuid
#import stripe

from django.conf import settings
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

		context = {
			'room': room,
			'seats': seats,
			'event': event,
			'booked_seats': booked_seats
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
		checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {'name': 'Make waves with WaveNetork'},
                        'unit_amount': total,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                billing_address_collection='required',
                payment_intent_data={'description': description},
                success_url=request.build_absolute_uri(reverse('cart:new_order')) +
                             f"?session_id={{CHECKOUT_SESSION_ID}}&voucher_id={voucher_id}&cart_total={total}",
                cancel_url=request.build_absolute_uri(reverse('cart:cart_detail')),
            )

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