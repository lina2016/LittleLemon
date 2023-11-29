from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.SingleMenuItemView, name="menu_item"),  
    path('bookings', views.bookings, name='bookings'), 
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]
