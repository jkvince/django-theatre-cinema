from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render

from accounts.models import CustomUser


class AdminBaseView(PermissionRequiredMixin):
	# Abstract class for admin pages
	permission_required = 'accounts.CustomUser'
	login_url = 'accounts:login' # should redirect to profile first


class AdminMainView(AdminBaseView, TemplateView):
	template_name = 'main.html'

class AdminUserView(AdminBaseView, ListView):
	template_name = 'user.html'
	model = CustomUser
	context_object_name = 'user_list'

	def get(self, request):
		context = {'users': CustomUser.objects.all()}
		return render(request, 'user.html', context)
