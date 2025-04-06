from django.urls import path
from .views import (
    AdminMainView,

    AdminUserListView, 
    AdminUserView,

    AdminShowListView,
    AdminShowView,
    AdminShowEdit,

    AdminEventListView,
    AdminEventView,

    AdminVenueListView,
    AdminVenueView,
    AdminRoomView,

    ShowMemberListView,
    ShowMemberView,
    OrderListView

    )

app_name = 'customadmin'

urlpatterns = [
    path('', AdminMainView.as_view(), name='admin_main'),

    path('users/', AdminUserListView.as_view(), name='admin_user_list'),
    path('users/<int:pk>/', AdminUserView.as_view(), name='admin_user'),

    path('shows/', AdminShowListView.as_view(), name='admin_show_list'),
    path('shows/<slug:pk>', AdminShowView.as_view(), name='admin_show'),
    path('shows/<slug:pk>/edit', AdminShowEdit.as_view(), name='admin_show_edit'),

    path('events/', AdminEventListView.as_view(), name='admin_event_list'),
    path('events/<int:pk>', AdminEventView.as_view(), name='admin_event'),

    path('venues/', AdminVenueListView.as_view(), name='admin_venue_list'),
    path('venues/<slug:pk>', AdminVenueView.as_view(), name='admin_venue'),
    path('room/<slug:pk>', AdminRoomView.as_view(), name='admin_room'),

    path('showmembers/', ShowMemberListView.as_view(), name='admin_showmember_list'),
    path('showmembers/<slug:pk>', ShowMemberView.as_view(), name='admin_showmember'),

    path('orders/', OrderListView.as_view(), name='admin_order_list')
]
