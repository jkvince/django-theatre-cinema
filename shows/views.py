from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Show

def show_page(request, pk):
	context = {
		'current_show': Show.objects.get(pk=pk),
		}
	return render(request, 'show.html', context)
