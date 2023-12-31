from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm

def form(request):
    comment_form = CommentForm()
    return render(request, "form.html", {"comment_form": comment_form})

def goal(request):
    if request.method != "POST":
        return HttpResponse("Metodo no permitido")

    return HttpResponse(request.POST["name"]) 

def widget(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, "widget.html", {"form": form})
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #Aqui se integran todas las acciones a realizar, cuando los datos son correctos
            return HttpResponse("Valido")
        else:
            #Aqui se comunica al usuario que los datos no son validados u otra accion cuando no es valida
            return HttpResponse("No es valido padrino")