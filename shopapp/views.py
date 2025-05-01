from datetime import datetime
import uuid
import stripe

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q, Count
from django.urls import reverse
from stripe import StripeError

from shows.models import Show
from venues.models import Event, Venue, Seat, Room, BookedSeat
from .models import Order

from django.http import HttpResponse

class HomePageView(ListView):
	model = Show
	context_object_name = 'show_list'
	template_name = 'home.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		if query:
			return Show.objects.filter(
				Q(show_name__icontains=query),
				public = True
			)
		else:
			return None


def trending_page_view(request):
	shows = Show.objects.annotate(
		num_booked=Count('event__bookedseat')
		).order_by('-num_booked').filter(public=1)[:5]

	context = {
		'shows': shows
	}
	return render(request, 'trending.html', context)


def event_page_view(request, pk):
	# user shouldn't be able to book without being logged in
	if not request.user.is_authenticated:
		return redirect('accounts:login')

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
		total = int(total * 100) # stripe doesnt use float point 

		stripe.api_key = settings.STRIPE_SECRET_KEY

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
                payment_intent_data={'description': "Description"},
                success_url=request.build_absolute_uri(reverse('shopapp:home')) +
                             f"?session_id={{CHECKOUT_SESSION_ID}}", #&voucher_id={voucher_id}&cart_total={total}",
                cancel_url=request.build_absolute_uri(reverse('shopapp:home')),
            )

		return redirect(checkout_session.url, code=303)


		#---
		order = Order.objects.create(
			order_id=uuid.uuid4(), 
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



def venues_page_view(request):
	context = {
		'venues': Venue.objects.all()
	}
	return render(request, 'venues.html', context)


def finalize_order(request):
	try:
		session_id = request.GET.get('session_id')
		if not session_id:
			raise ValueError("Session ID not found.")

		try:
			session = stripe.checkout.Session.retrieve(session_id)
		except StripeError as e:
			print(f"Error: {e}")
			return redirect("shopapp:home")

		customer_details = session.customer_details
		if not customer_details or not customer_details.address:
			raise ValueError("Missing information in the Stripe session.")

		try:
			order = Order.objects.create(
				order_id=uuid.uuid4(), 
				user=request.user,
				total=float(session.amount_total) / 100,

				billing_name=customer_details.name,
				billing_address=customer_details.address,
				billing_city='',
				billing_postcode='',
				billing_country=''
			)

		except Exception as e:
			print(f"Error: {e}")
			return redirect("shopapp:home")

		try:
			cart = Cart.objects.get(cart_id=_cart_id(request))
			cart_items = CartItem.objects.filter(cart=cart, active=True)
		
		except ObjectDoesNotExist:
			return redirect("shopapp:home")
		
		except Exception as e:
			print(f"Error: {e}")
			return redirect("shopapp:home")

		for item in cart_items:
			try:
				oi = OrderItem.objects.create(
					product=item.product.name,
					quantity=item.quantity,
					price=item.product.price,
					order=order_details
				)

				empty_cart(request)

			except Exception as e:
				return redirect("shopapp:home")

		# send email 
		return redirect("shopapp:home")

	except ValueError as ve:
		print(f"Error: {ve}")
		return redirect("shopapp:home")

	except StripeError as se:
		print(f"Stripe Error: {se}")
		return redirect("shopapp:home")

	except Exception as e:
		print(f"Unexpected error: {e}")
		return redirect("shopapp:home")