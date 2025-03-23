from django.shortcuts import render

from .models import Show

def show_page(request, pk):
	try:
		query = Show.objects.get(pk=pk)
		if query.public == True:
			context = {
				'current_show': query,
			}
			return render(request, 'show.html', context)
		else:
			return render(request, '404.html')
			
	except:
		return render(request, '404.html')
