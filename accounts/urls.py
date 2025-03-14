from django.urls import path, include
from .views import SignUpView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile', ProfileView.as_view(), name='profile'),
]