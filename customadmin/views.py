from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from accounts.models import CustomUser


class AdminMainPage(PermissionRequiredMixin, TemplateView):
	template_name = 'main_admin.html'
	permission_required = 'accounts.CustomUser'
	raise_exception = True
	login_url = 'accounts/login'
