from django.urls import path
from .views import (
    AdminMainView,

    AdminUserListView, 
    AdminUserView,
    AdminUserCreateView,
    AdminUserEditView,

    AdminShowListView,
    AdminShowView,
    AdminShowCreateView,
    AdminShowEditView,

    AdminEventListView,
    AdminEventView,
    AdminEventCreateView,
    AdminEventEditView,

    AdminVenueListView,
    AdminVenueView,
    AdminVenueCreateView,
    AdminVenueEditView,
    AdminRoomView,

    AdminShowMemberListView,
    AdminShowMemberView,
    AdminShowMemberCreateView,
    AdminShowMemberEditView,

    AdminOrderListView,
    AdminOrderView

    )

app_name = 'customadmin'

urlpatterns = [
    path('', AdminMainView.as_view(), name='admin_main'),

    path('users/', AdminUserListView.as_view(), name='admin_user_list'),
    path('users/<int:pk>/', AdminUserView.as_view(), name='admin_user'),
    path('userscreate/', AdminUserCreateView.as_view(), name='admin_user_create'),
    path('users/<int:pk>/edit', AdminUserEditView.as_view(), name='admin_user_edit'),

    path('shows/', AdminShowListView.as_view(), name='admin_show_list'),
    path('shows/<slug:pk>', AdminShowView.as_view(), name='admin_show'),
    path('showscreate/', AdminShowCreateView.as_view(), name='admin_show_create'),
    path('shows/<slug:pk>/edit', AdminShowEditView.as_view(), name='admin_show_edit'),

    path('events/', AdminEventListView.as_view(), name='admin_event_list'),
    path('events/<int:pk>', AdminEventView.as_view(), name='admin_event'),
    path('eventscreate/', AdminEventCreateView.as_view(), name='admin_event_create'),
    path('events/<int:pk>/edit', AdminEventEditView.as_view(), name='admin_event_edit'),

    path('venues/', AdminVenueListView.as_view(), name='admin_venue_list'),
    path('venues/<slug:pk>', AdminVenueView.as_view(), name='admin_venue'),
    path('venuescreate', AdminVenueCreateView.as_view(), name='admin_venue_create'),
    path('venues/<slug:pk>/edit', AdminVenueEditView.as_view(), name='admin_venue_edit'),
    path('room/<slug:pk>', AdminRoomView.as_view(), name='admin_room'),

    path('showmembers/', AdminShowMemberListView.as_view(), name='admin_showmember_list'),
    path('showmembers/<slug:pk>', AdminShowMemberView.as_view(), name='admin_showmember'),
    path('showmemberscreate/', AdminShowMemberCreateView.as_view(), name='admin_showmember_create'),
    path('showmembers/<slug:pk>/edit', AdminShowMemberEditView.as_view(), name='admin_showmember_edit'),

    path('orders/', AdminOrderListView.as_view(), name='admin_order_list'),
    path('orders/<uuid:pk>', AdminOrderView.as_view(), name='admin_order')
]
