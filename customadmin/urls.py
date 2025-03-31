from django.urls import path
from .views import (
    AdminMainView,

    AdminUserListView, 
    AdminUserView,

    AdminShowListView,
    AdminShowView,

    AdminEventListView,
    AdminEventView,

    AdminVenueListView,
    AdminVenueView,
    AdminRoomView

    )

app_name = 'customadmin'

urlpatterns = [
    path('', AdminMainView.as_view(), name='admin_main'),

    path('users/', AdminUserListView.as_view(), name='admin_user_list'),
    path('users/<int:pk>/', AdminUserView.as_view(), name='admin_user'),

    path('shows/', AdminShowListView.as_view(), name='admin_show_list'),
    path('shows/<str:pk>', AdminShowView.as_view(), name='admin_show'),

    path('events/', AdminEventListView.as_view(), name='admin_event_list'),
    path('events/<int:pk>', AdminEventView.as_view(), name='admin_event'),

    path('venues/', AdminVenueListView.as_view(), name='admin_venue_list'),
    path('venues/<str:pk>', AdminVenueView.as_view(), name='admin_venue'),

    path('room/<str:pk>', AdminRoomView.as_view(), name='admin_room')
]
