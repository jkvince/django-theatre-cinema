from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.shortcuts import render, redirect
from django.db.models import Avg

from accounts.models import CustomUser
from shows.models import Show, ShowMember, MemberJunction, Comment, Rating, Following
from venues.models import Event


class AdminAbstractView(PermissionRequiredMixin, TemplateView):
	# Abstract class for admin pages
	permission_required = 'accounts.CustomUser.is_staff'


class AdminMainView(AdminAbstractView):
	template_name = 'main.html'

class AdminUserListView(AdminAbstractView):
	def get(self, request):
		context = {'users': CustomUser.objects.all()}
		return render(request, 'user/list.html', context)

class AdminUserView(AdminAbstractView):
	def get(self, request, pk):
		context = {
			'current_user': CustomUser.objects.get(pk=pk),
			'user_comments': Comment.objects.filter(user_id=pk)
			}
		return render(request, 'user/user.html', context)

class AdminShowListView(AdminAbstractView):
	def get(self, request):
		context = {'shows': Show.objects.all().order_by('-show_release_date')}
		return render(request, 'show/list.html', context)

class AdminShowView(AdminAbstractView):
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

	def post(self, request, pk):
		context = {}
		if 'delete_comment' in request.POST:
			comment_id = request.POST.get('delete_comment')
			Comment.objects.get(comment_id=comment_id, show_id=pk).delete()
			print("Comment:", comment_id, "has been deleted")

		elif 'delete_rating' in request.POST:
			rating_id = request.POST.get('delete_rating')
			Rating.objects.get(rating_id=rating_id, show_id=pk).delete()
			print("Rating:", rating_id, "has been deleted")
		
		return redirect('customadmin:admin_show', pk)

class AdminEventListView(AdminAbstractView):
	def get(self, request):
		context = {'events': Event.objects.all()}
		return render(request, 'event/list.html', context)

class AdminEventView(AdminAbstractView):
	def get(self, request, pk):
		context = {
			'event': Event.objects.get(pk=pk)
		}
		return render(request, 'event/event.html', context)