from django.urls import path
from .views import HomePageView, LoginPageView, SignUpView

app_name = 'accounts'

urlpatterns = [
	path('', SignUpView.as_view(), name='signup'),
    path('login', LoginPageView.as_view(), name='login')
]