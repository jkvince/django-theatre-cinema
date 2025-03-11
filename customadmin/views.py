from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import CustomUser


class AdminMainPage(TemplateView, LoginRequiredMixin):
	template_name = 'main.html'