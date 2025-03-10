from django.urls import path
from .views import LoginPageView, SignUpView, HomePageView

app_name = 'accounts'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login', LoginPageView.as_view(), name='login'),
    path('signup', SignUpView.as_view(), name='signup')
]