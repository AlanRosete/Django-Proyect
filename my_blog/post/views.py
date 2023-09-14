from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry


def update(request):
    author = Author.objects.get(id=1)
    author.name = "Juanjo"
    author.email = "juanjo@demo.com"
    author.save()
    return HttpResponse("Modificado")

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

    #Obtener todos los elementos donde el ID sea menor o igual a 15
    #
    filtered = Author.objects.filter(id__lte=15) #En este ejemplo se muestran los primeros 15 resultados
    # VALORES DE EQUAL    
    __lte = 20 #menor o igual que 
    __gte = 20 #mayor o igual que
    __lt = 20 #menor que 
    __gt = 20 #mayor que
    __countains = 20 #contiene
    __exact = 20 #Valor exacto
    # FIN


    return render(request, "post/queries.html", {"authors": authors, "filtered": filtered, "author": author})

    

    
    