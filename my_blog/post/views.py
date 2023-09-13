from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

def queries(request):
    #Obtener todos los documentos 
    authors = Author.objects.all()

    #Realizar el filtrado de algun correo en especifico de la base de datos

    filtered = Author.objects.filter(email="aking@example.net")

    #Obtener un unico valor por ID

    author = Author.objects.get(id=1)

    #Se realiza la estructura pero todos estos no estan declarados

    #Obtener los primeros 10 elementos

    limits = Author.objects.all()[:10]

    #Obtener los 5 elementos saltando los primeros 5 elementos de la tabla

    offset = Author.objects.all()[5:10]

    #Obtener todos los resultados de una forma ordenada

    orders = Author.objects.all().order_by("email") #Se realiza la ordenacion de los correos de forma alfabetica


    return render(request, "post/queries.html", {"authors": authors, "filtered": filtered, "author": author})
# Create your views here.
