from django.views.generic import View, CreateView, UpdateView
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest

from django.shortcuts import render, redirect
from django.db.models import Avg, Count

from accounts.models import CustomUser
from shows.models import Show, ShowMember, Comment, Rating, Following
from venues.models import Venue, Room, Seat, Event, BookedSeat
from shopapp.models import Order

import json

class AdminAbstractView(PermissionRequiredMixin, View):
	# Abstract class for admin pages
	permission_required = 'accounts.CustomUser.is_staff'


class AdminMainView(AdminAbstractView):
	def get(self, request):
		# 10 most booked shows of all time
		most_booked = Show.objects.annotate(
			num_booked=Count('event__bookedseat')
		).order_by('-num_booked')[:10]




		context = {
			"most_booked": most_booked
		}
		return render(request, 'main.html', context)

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

	def post(self, request, pk):
		if 'delete_user' in request.POST:
			user_id = request.POST.get('delete_user')
			CustomUser.objects.get(pk=user_id).delete()
			print("User `" + user_id +"` has been deleted")
			return redirect('customadmin:admin_user_list')

class AdminUserCreateView(CreateView, AdminAbstractView):
	model = CustomUser
	fields = [
		'username', 'email', 'phone', 'is_premium', 'is_staff'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Create User"}
	success_url = reverse_lazy('customadmin:admin_user_list')


class AdminUserEditView(UpdateView, AdminAbstractView):
	model = CustomUser
	fields = [
		'username', 'email', 'phone', 'is_premium', 'is_staff'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Edit User"}
	success_url = reverse_lazy('customadmin:admin_user_list')

class AdminShowListView(AdminAbstractView):
	def get(self, request):
		context = {'shows': Show.objects.all().order_by('show_name')}
		return render(request, 'show/list.html', context)

class AdminShowView(AdminAbstractView):
	def get(self, request, pk):
		current_show = Show.objects.get(pk=pk)
		context = {
			'current_show': current_show,
			'show_comments': Comment.objects.filter(show_id=pk),
			'show_followers': Following.objects.filter(show_id=pk),
			'ratings': Rating.objects.filter(show_id=pk),
			#'showmembers': current_show.show_member.all(),

			'followers_amount': Following.objects.filter(show_id=pk).count(),
			'average_rating': Rating.objects.filter(show_id=pk).aggregate(Avg('rating_value'))['rating_value__avg']
			}
		return render(request, 'show/show.html', context)

	def post(self, request, pk):
		if 'delete_comment' in request.POST:
			comment_id = request.POST.get('delete_comment')
			Comment.objects.get(comment_id=comment_id, show_id=pk).delete()
			print("Comment `" + str(comment_id) +"` has been deleted")
			return redirect('customadmin:admin_show', pk)

		elif 'delete_rating' in request.POST:
			rating_id = request.POST.get('delete_rating')
			Rating.objects.get(rating_id=rating_id, show_id=pk).delete()
			print("Rating `" + str(rating_id) + "` has been deleted")
			return redirect('customadmin:admin_show', pk)

		elif 'delete_show' in request.POST and request.POST.get('delete_show') == pk:
			Show.objects.get(pk=pk).delete()
			print("Show `" + str(pk) + "` has been deleted")
			return redirect('customadmin:admin_show_list')

class AdminShowCreateView(CreateView, AdminAbstractView):
	model = Show
	fields = [
		'show_name', 'show_duration', 'show_description', 'show_agerating', 'show_release_date',
		'show_type', 'show_language', 'show_banner', 'public'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Create Show"}
	success_url = reverse_lazy('customadmin:admin_show_list')

	def form_valid(self, form):
		form.instance.show_id = slugify(form.instance.show_name)
		#form.instance.show_banner = {'mugshot': SimpleUploadedFile('face.jpg', <file data>)}
		print("Show created: `" + form.instance.show_id + "`")
		return super().form_valid(form)

class AdminShowEditView(UpdateView, AdminAbstractView):
	model = Show
	fields = [
		'show_name', 'show_duration', 'show_description', 'show_agerating', 'show_release_date',
		'show_type', 'show_language', 'show_banner', 'public'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Edit Show"}
	success_url = reverse_lazy('customadmin:admin_show_list')

	#def get_success_url(self):
	#	return reverse_lazy('customadmin:admin_show', kwargs={'pk': self.object.branch.id})


#	def post(self, request, pk):
#		show = Show.objects.get(pk=pk)
#		show.show_name = request.POST.get('show_name')
#		show.show_duration = request.POST.get('show_duration')
#		show.show_type = request.POST.get('show_type')
#		show.show_description = request.POST.get('show_description')
#		show.show_agerating = request.POST.get('show_agerating')
#		show.show_release_date = request.POST.get('show_release_date')
#		show.show_language = request.POST.get('show_language')
#
#		banner = request.POST.get('show_banner')
#		if banner != "":
#			show.show_banner = {
#				'name': banner,
#				'img': request.FILES
#			}
#
#		public = request.POST.get('public')
#		if public == 'on':
#			show.public = True
#		elif public == None:
#			show.public = False
#		show.save()
#		return redirect('customadmin:admin_show', pk)



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

class AdminEventCreateView(CreateView, AdminAbstractView):
	model = Event
	fields = [
		'show', 'room_number', 'event_time', 'price', 'public'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Create Event"}
	success_url = reverse_lazy('customadmin:admin_event_list')

class AdminEventEditView(UpdateView, AdminAbstractView):
	model = Event
	fields = [
		'show', 'room_number', 'event_time', 'price', 'public'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Edit Event"}
	success_url = reverse_lazy('customadmin:admin_event_list')

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

	def post(self, request, pk):
		if 'create_room' in request.POST:
			room_number = request.POST.get('create_room')
			venue = Venue.objects.get(pk=pk)
			Room.objects.create(
				room_id=venue.venue_id + "-" + slugify(room_number),
				venue_id=venue,
				room_number=room_number
			)
			print("Room `" + room_number + "` has been created for venue `" + venue.venue_id + "`")
			return redirect('customadmin:admin_venue', pk)

		elif 'delete_room' in request.POST:
			room_number = request.POST.get('delete_room')
			Room.objects.get(pk=room_number).delete()
			print("Room `" + room_number + "` has been deleted")
			return redirect('customadmin:admin_venue', pk)

		elif 'delete_venue' in request.POST:
			venue_id = request.POST.get('delete_venue')
			Venue.objects.get(pk=venue_id).delete()
			print("Venue `" + venue_id + "` has been deleted")
			return redirect('customadmin:admin_venue_list')


class AdminVenueCreateView(CreateView, AdminAbstractView):
	model = Venue
	fields = [
		'venue_name', 'venue_address', 'working_hours', 'venue_latitude', 'venue_longitude',
		'venue_contact', 'venue_accessibility', 'public'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Create Venue"}
	success_url = reverse_lazy('customadmin:admin_venue_list')

	def form_valid(self, form):
		form.instance.venue_id = slugify(form.instance.venue_name)
		print("Venue created: `" + form.instance.venue_id + "`")
		return super().form_valid(form)

class AdminVenueEditView(UpdateView, AdminAbstractView):
	model = Venue
	fields = [
		'venue_name', 'venue_address', 'working_hours', 'venue_latitude', 'venue_longitude',
		'venue_contact', 'venue_accessibility', 'public'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Edit Venue"}
	success_url = reverse_lazy('customadmin:admin_venue_list')

class AdminRoomView(AdminAbstractView):
	def get(self, request, pk):
		room = Room.objects.get(pk=pk)
		seats = Seat.objects.filter(room_number=room.room_id)

		context = {
			'room': room,
			'seats': seats
		}
		return render(request, 'venue/room.html', context)

	def post(self, request, pk):
		rows = int(request.POST.get('grid-row'))
		columns = int(request.POST.get('grid-col'))
		grid_info = json.loads(request.POST.get('grid-info'))


		# check if all seat numbers are not empty
		for seat in grid_info:
			if seat["number"] == "" or seat["number"] == None:
				return HttpResponseBadRequest("There has been an error. A seat had an empty name.")

		# check if there are any matching seat numbers
		number_list = [x["number"] for x in grid_info]
		if len(number_list) != len(set(number_list)):
			return HttpResponseBadRequest("There has been an error. Multiple seats had matching names.")

		# update rows and columns of room
		room = Room.objects.get(pk=pk)
		room.room_rows = rows
		room.room_columns = columns
		room.save()

		# delete all previous seats
		Seat.objects.filter(room_number=pk).delete()

		# create database seats
		for seat in grid_info:
			Seat.objects.create(
				room_number=room,
				seat_id=pk + "-" + slugify(seat["number"]),
				seat_number=seat["number"],
				seat_premium=seat["premium"],
				seat_accessible=seat["accessible"],
				location_row=seat["location_row"],
				location_column=seat["location_column"]
			)

		return redirect('customadmin:admin_room', pk)


class AdminShowMemberListView(AdminAbstractView):
	def get(self, request):
		context = {'showmembers': ShowMember.objects.all().order_by('show_member_name')}
		return render(request, 'showmember/list.html', context)

class AdminShowMemberView(AdminAbstractView):
	def get(self, request, pk):
		showmember = ShowMember.objects.get(pk=pk)
		shows = showmember.shows.all()
		context = {
			'showmember': showmember,
			'shows': shows
		}
		return render(request, 'showmember/showmember.html', context)

class AdminShowMemberCreateView(CreateView, AdminAbstractView):
	model = ShowMember
	fields = [
		'show_member_name', 'show_member_type', 'shows', 'public',
		'show_member_banner'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Create ShowMember"}
	success_url = reverse_lazy('customadmin:admin_showmember_list')

	def form_valid(self, form):
		form.instance.show_member_id = slugify(form.instance.show_member_name)
		print("ShowMember created: `" + form.instance.show_member_id + "`")
		return super().form_valid(form)

class AdminShowMemberEditView(UpdateView, AdminAbstractView):
	model = ShowMember
	fields = [
		'show_member_name', 'show_member_type', 'shows', 'public',
		'show_member_banner'
	]
	template_name = 'form.html'
	extra_context = {"form_title": "Edit ShowMember"}
	success_url = reverse_lazy('customadmin:admin_showmember_list')


class AdminOrderListView(AdminAbstractView):
	def get(self, request):
		context = {'orders': Order.objects.all()}
		return render(request, 'order/list.html', context)

class AdminOrderView(AdminAbstractView):
	def get(self, request, pk):
		order = Order.objects.get(pk=pk)
		seats = BookedSeat.objects.filter(order_id=order)
		context = {
			'order': order,
			'seats': seats
		}
		return render(request, 'order/order.html', context)