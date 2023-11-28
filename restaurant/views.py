from django.shortcuts import render
from .forms import BookingForm
from django.core import serializers
from django.db import models
from datetime import datetime
#import json
#from django.views.decorators.csrf import csrf_exempt
#from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def SingleMenuItemView(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

# class MenuView(generics.ListCreateAPIView):
#    permission_classes = [IsAuthenticated]
#    queryset = Menu.objects.all()
#    serializer_class = MenuSerializer
   
# @csrf_exempt
# def bookings(request):
#     if request.method == 'POST':
#         data = json.load(request)
#         exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
#             reservation_slot=data['reservation_slot']).exists()
#         if exist==False:
#             booking = Booking(
#                 first_name=data['first_name'],
#                 reservation_date=data['reservation_date'],
#                 reservation_slot=data['reservation_slot'],
#             )
#             booking.save()
#         else:
#             return HttpResponse("{'error':1}", content_type='application/json')
    
#     date = request.GET.get('date',datetime.today().date())

#     bookings = Booking.objects.all().filter(reservation_date=date)
#     booking_json = serializers.serialize('json', bookings)

#     return HttpResponse(booking_json, content_type='application/json')