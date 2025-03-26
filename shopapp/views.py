from django.shortcuts import render
from django.views.generic import TemplateView

from shows.models import Show
from venues.models import Event

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
		context = {
			'event': Event.objects.get(pk=pk)
		}
		return render(request, 'event.html', context)