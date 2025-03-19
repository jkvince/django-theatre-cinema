from django.shortcuts import render
from django.views.generic import TemplateView

from shows.models import Show

class HomePageView(TemplateView):
	template_name = 'home.html'

class TrendingPageView(TemplateView):
	def get(self, request):
		context = {'shows': Show.objects.all()}
		return render(request, 'trending.html', context)
