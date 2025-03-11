from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

	
class LoginPageView(CreateView):
	template_name = 'registration/login.html'
	model = CustomUser
	fields = [
		'username',
		'password',
		]
		

class SignUpView(CreateView):
	model = CustomUser
	form_class = CustomUserCreationForm
	template_name = 'registration/signup.html'
	success_url = reverse_lazy('accounts:home')

	def form_valid(self, form):
		# Save the new user
		response = super().form_valid(form)
		# Log the user in after signup
		login(self.request, self.object)
		return response # Redirect to success URL


class HomePageView(TemplateView):
	template_name = 'registration/index.html'

class VenuesView(TemplateView):
	template_name = 'registration/venues.html'