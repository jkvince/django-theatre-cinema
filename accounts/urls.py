from django.urls import path, include
from .views import SignUpView, HomePageView

app_name = 'accounts'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]