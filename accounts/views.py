from django.views.generic import TemplateView, CreateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

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
	
class LoginPageView(CreateView):
	template_name = 'login.html'
	model = CustomUser
	fields = [
		'username',
		'email',
		'password',
		'premium',
		'profile_pic'
		]