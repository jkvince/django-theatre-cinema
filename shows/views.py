from django.shortcuts import render

from .models import Show
from shows.models import Comment
from venues.models import Event

def show_page(request, pk):
	try:
		query = Show.objects.get(pk=pk)
		if query.public == True:
			context = {
				'current_show': query,
				'comments': Comment.objects.filter(show_id=pk),
				'events': Event.objects.filter(show_id=pk).order_by('price')
			}
			return render(request, 'show.html', context)
		else:
			return render(request, '404.html')

	except:
		return render(request, '404.html')
