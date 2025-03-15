from django.urls import path
from .views import AdminMainView, AdminUserView
app_name = 'customadmin'

urlpatterns = [
    path('', AdminMainView.as_view(), name='admin_main'),
    path('users/', AdminUserView.as_view(), name='admin_user'),
]
