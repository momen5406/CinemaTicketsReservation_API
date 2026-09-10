from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Movie, Guest, Reservation


#1 Without REST and no model query FBV
def no_rest_no_model(request):
    guests = [
        {
            'id': 1,
            'name': 'Ahmed',
            'mobile': '0123456789'
        },
        {
            'id': 2,
            'name': 'Omar',
            'mobile': '0268101214'
        }
    ]

    return JsonResponse(guests, safe=False)


#2 Without Rest and from Model
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        "guests": list(data.values("name", "mobile"))
    }
    return JsonResponse(response)