from django.http.response import JsonResponse
from rest_framework import status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie, Guest, Reservation
from .serializers import  GuestSerializer, MovieSerializer, ReservationSerializer


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


#3 With Rest (Functional Based Views)
#3.1 GET POST
@api_view(['GET', 'POST'])
def fbv_list(request):
    # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#3.2 GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def fbv_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)