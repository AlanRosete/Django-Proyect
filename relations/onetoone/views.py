from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Restaurant

# Create your views here.

def create(request):
    #Se realiza toda la creacion de los elementos
    place = Place(name="1er Lugar", adress="Calle Quinta Sinfonia")
    place.save()

    restaurant = Restaurant(place=place, number_of_employees=8)
    restaurant.save()

    return HttpResponse(restaurant.place.name)


