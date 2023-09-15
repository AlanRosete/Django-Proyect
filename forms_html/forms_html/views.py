from django.shortcuts import render
from django.http import HttpResponse

def getform(request):
    return render(request, "form.html", {})

def getgoal(request):
    if request == "GET":
        return render(request, "success.html", {})
    else:
        return HttpResponse("Te falta calle padrino")
    
def postform(request):
    return render(request, "postform.html", {})

def postgoal(request): 

    if request.method != "POST":
        return HttpResponse("El metodo GET no esta soportado para esta ruta")

    info = request.POST["info"]
    return render(request, "postsuccess.html", {"info": info})