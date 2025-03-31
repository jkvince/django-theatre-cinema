from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.shortcuts import render, redirect
from django.db.models import Avg

from accounts.models import CustomUser
from shows.models import Show, ShowMember, MemberJunction, Comment, Rating, Following
from venues.models import Venue, Room, Seat, Event, BookedSeat


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
		context = {'shows': Show.objects.all().order_by('show_name')}
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
		if 'delete_comment' in request.POST:
			comment_id = request.POST.get('delete_comment')
			Comment.objects.get(comment_id=comment_id, show_id=pk).delete()
			print("Comment:", comment_id, "has been deleted")
			return redirect('customadmin:admin_show', pk)

		elif 'delete_rating' in request.POST:
			rating_id = request.POST.get('delete_rating')
			Rating.objects.get(rating_id=rating_id, show_id=pk).delete()
			print("Rating:", rating_id, "has been deleted")
			return redirect('customadmin:admin_show', pk)

		elif 'delete_show' in request.POST and request.POST.get('delete_show') == pk:
			Show.objects.get(pk=pk).delete()
			print("Show:", pk, "has been deleted")
			return redirect('customadmin:admin_show_list')


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


class AdminVenueListView(AdminAbstractView):
	def get(self, request):
		context = {'venues': Venue.objects.all()}
		return render(request, 'venue/list.html', context)


class AdminVenueView(AdminAbstractView):
	def get(self, request, pk):
		context = {
			'venue': Venue.objects.get(pk=pk),
			'rooms': Room.objects.filter(venue_id=pk)
		}
		return render(request, 'venue/venue.html', context)


class AdminRoomView(AdminAbstractView):
	def get(self, request, pk):
		room = Room.objects.get(pk=pk)
		grid = [[None for y in range(room.room_columns)] for x in range(room.room_rows)]

		seats = Seat.objects.filter(room_number=room.room_id)

		for seat in seats:
			grid[seat.location_row][seat.location_column] = {'seat': seat}

		context = {
			'room': room,
			'grid': grid
		}
		return render(request, 'venue/room.html', context)
