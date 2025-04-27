from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .models import CustomUser
from shopapp.models import Order
from venues.models import Seat

from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
	model = CustomUser
	form_class = CustomUserCreationForm
	template_name = 'signup.html'
	success_url = reverse_lazy('shopapp:home')

	def form_valid(self, form):
		# Save the new user
		response = super().form_valid(form)
		# Log the user in after signup
		login(self.request, self.object)
		return response # Redirect to success URL


class ProfileView(LoginRequiredMixin, TemplateView):
	def get(self, request):
		orders = Order.objects.filter(user=request.user)

		context = {
			"orders": orders
		}
		return render(request, 'profile.html', context)
