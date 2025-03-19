from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Avg

from accounts.models import CustomUser
from shows.models import Show, ShowMember, MemberJunction, Comment, Rating, Following


class AdminBaseView(PermissionRequiredMixin, TemplateView):
	# Abstract class for admin pages
	permission_required = 'accounts.CustomUser'


class AdminMainView(AdminBaseView):
	template_name = 'main.html'

class AdminUserListView(AdminBaseView):
	def get(self, request):
		context = {'users': CustomUser.objects.all()}
		return render(request, 'user/list.html', context)

class AdminUserView(AdminBaseView):
	def get(self, request, pk):
		context = {
			'current_user': CustomUser.objects.get(pk=pk),
			'user_comments': Comment.objects.filter(user_id=pk)
			}
		return render(request, 'user/user.html', context)

class AdminShowListView(AdminBaseView):
	def get(self, request):
		context = {'shows': Show.objects.all()}
		return render(request, 'show/list.html', context)

class AdminShowView(AdminBaseView):
	def get(self, request, pk):
		context = {
			'current_show': Show.objects.get(pk=pk),
			'show_comments': Comment.objects.filter(show_id=pk),
			'show_followers': Following.objects.filter(show_id=pk),
			'ratings': Rating.objects.filter(show_id=pk),

			'followers_amount': Following.objects.filter(show_id=pk).count(),
			'average_rating': Rating.objects.filter(show_id=pk).aggregate(Avg('rating_value'))['rating_value__avg']
			}
		return render(request, 'show/show.html', context)