from django.urls import path
from .views import (
    AdminMainView,

    AdminUserListView, 
    AdminUserView,

    AdminShowListView,
    AdminShowView,
    AdminShowCreateView,
    AdminShowEditView,

    AdminEventListView,
    AdminEventView,

    AdminVenueListView,
    AdminVenueView,
    AdminRoomView,

    AdminShowMemberListView,
    AdminShowMemberView,


    AdminOrderListView,
    AdminOrderView

    )

app_name = 'customadmin'

urlpatterns = [
    path('', AdminMainView.as_view(), name='admin_main'),

    path('users/', AdminUserListView.as_view(), name='admin_user_list'),
    path('users/<int:pk>/', AdminUserView.as_view(), name='admin_user'),

    path('shows/', AdminShowListView.as_view(), name='admin_show_list'),
    path('shows/<slug:pk>', AdminShowView.as_view(), name='admin_show'),
    path('showcreate/', AdminShowCreateView.as_view(), name='admin_show_create'),
    path('shows/<slug:pk>/edit', AdminShowEditView.as_view(), name='admin_show_edit'),

    path('events/', AdminEventListView.as_view(), name='admin_event_list'),
    path('events/<int:pk>', AdminEventView.as_view(), name='admin_event'),

    path('venues/', AdminVenueListView.as_view(), name='admin_venue_list'),
    path('venues/<slug:pk>', AdminVenueView.as_view(), name='admin_venue'),
    path('room/<slug:pk>', AdminRoomView.as_view(), name='admin_room'),

    path('showmembers/', AdminShowMemberListView.as_view(), name='admin_showmember_list'),
    path('showmembers/<slug:pk>', AdminShowMemberView.as_view(), name='admin_showmember'),

    path('orders/', AdminOrderListView.as_view(), name='admin_order_list'),
    path('orders/<uuid:pk>', AdminOrderView.as_view(), name='admin_order')
]
