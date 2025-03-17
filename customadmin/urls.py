from django.urls import path
from .views import (
    AdminMainView, 
    AdminUserListView, 
    AdminUserView,
    AdminShowListView,
    AdminShowView
    )

app_name = 'customadmin'

urlpatterns = [
    path('', AdminMainView.as_view(), name='admin_main'),
    path('users/', AdminUserListView.as_view(), name='admin_user_list'),
    path('users/<int:pk>/', AdminUserView.as_view(), name='admin_user'),
    path('shows/', AdminShowListView.as_view(), name='admin_show_list'),
    path('shows/<pk>', AdminShowView.as_view(), name='admin_show')
]
