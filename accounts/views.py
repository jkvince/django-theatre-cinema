from django.views.generic import TemplateView, CreateView
from .models import CustomUser

class HomePageView(CreateView):
	model = CustomUser
	template_name = 'home.html'
	fields = [
		'username',
		'email',
		'password',
		'premium',
		'profile_pic'
		]