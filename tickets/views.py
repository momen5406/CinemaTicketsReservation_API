from django.http.response import JsonResponse
from django.shortcuts import render


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