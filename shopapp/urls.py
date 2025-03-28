from django.urls import path
from .views import (
    HomePageView, 
    TrendingPageView,
    EventPageView,
    VenuesPageView
)

app_name = 'shopapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('trending/', TrendingPageView.as_view(), name='trending'),
    path('event/<int:pk>', EventPageView.as_view(), name='event'),
    #path('event/<int:pk>/', name='book_processing'),
    path('venues', VenuesPageView.as_view(), name='venues')
]