from django.urls import path
from .views import AdminMainPage
app_name = 'admin'

urlpatterns = [
    path('', AdminMainPage.as_view(), name='admin_main'),
]
