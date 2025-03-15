from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render

from accounts.models import CustomUser


class AdminBaseView(PermissionRequiredMixin, TemplateView):
	# Abstract class for admin pages
	permission_required = 'accounts.CustomUser'
	login_url = 'accounts:login' # should redirect to profile first


class AdminMainView(AdminBaseView):
	template_name = 'main.html'

class AdminUserListView(AdminBaseView):
	def get(self, request):
		context = {'users': CustomUser.objects.all()}
		return render(request, 'user_list.html', context)

class AdminUserView(AdminBaseView):
	def get(self, request, pk):
		context = {'current_user': CustomUser.objects.get(pk=pk)}
		return render(request, 'user.html', context)