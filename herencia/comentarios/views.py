from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse("Funciona Correctamente")

def create(request):

    comment = Comment(name="JuanGa", score=5, comments="Prueba Comentario")
    comment.save()

    #Otro metodo para realizar el objeto Class seria: 
    
    # comment = Comment.objects.create(name="JuanGa", score=5, comments="Prueba Comentario")

    return HttpResponse("Ruta para probar la creacion de modelos")

# Create your views here.
