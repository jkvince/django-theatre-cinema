from django.shortcuts import render
from django.views.generic import TemplateView

from shows.models import Show
from venues.models import Event, Venue, Seat, Room

class HomePageView(TemplateView):
	template_name = 'home.html'

class TrendingPageView(TemplateView):
	def get(self, request):
		context = {
			'shows': Show.objects.filter(public=1)
		}
		return render(request, 'trending.html', context)

class EventPageView(TemplateView):
	def get(self, request, pk):
		event = Event.objects.get(pk=pk)
		room = Room.objects.get(room_id=event.room_number)
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

class VenuesPageView(TemplateView):
	def get(self, request):
		context = {
			'venues': Venue.objects.all()
		}
		return render(request, 'venues.html', context)