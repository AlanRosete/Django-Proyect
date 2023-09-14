from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

# Create your views here.

def create(request):
    
    art1 = Article(headline="Articulo primero")
    art1.save()
    
    art2 = Article(headline="Articulo segundo")
    art2.save()
    
    art3 = Article(headline="Articulo tercero")
    art3.save()

    
    pub1 = Publication(title="Publicacion primera")
    pub1.save()
    pub2 = Publication(title="Publicacion segunda")
    pub2.save()
    pub3 = Publication(title="Publicacion tercera")
    pub3.save()
    pub4 = Publication(title="Publicacion cuarta")
    pub4.save()
    pub5 = Publication(title="Publicacion quinta")
    pub5.save()
    pub6 = Publication(title="Publicacion sexta")
    pub6.save()

    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)

    result = art1.publications.all()

    #Si se desea realizar la eliminacion de un art1 con cualquier pub que se requiera seria de la siguiente manera:
    # art1.publications.remove(pub2) en este caso se realiza la depuracion del pub2


    return HttpResponse(result)