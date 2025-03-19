from django.urls import path
from .views import show_page

app_name = 'shows'

urlpatterns = [
    path('<str:pk>', show_page, name='show_page')
]

