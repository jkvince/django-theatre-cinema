from django.urls import path
from .views import (
    HomePageView, 
    trending_page_view,
    event_page_view,
    venues_page_view
)

app_name = 'shopapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('trending/', trending_page_view, name='trending'),
    path('event/<int:pk>', event_page_view, name='event'),
    path('venues', venues_page_view, name='venues')
]