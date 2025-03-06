from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


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

class SignUpView(CreateView):
	model = CustomUser
	form_class = CustomUserCreationForm
	template_name = 'home.html'
	#success_url = reverse_lazy('shop:all_products')

	def form_valid(self, form):
		# Save the new user
		response = super().form_valid(form)
		# Add user to the Customer group
		customer_group, created = Group.objects.get_or_create(name='Customer')
		self.object.groups.add(customer_group)
		# Log the user in after signup
		login(self.request, self.object)
		return response # Redirect to success URL

