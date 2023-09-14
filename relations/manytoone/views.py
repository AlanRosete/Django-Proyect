from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name="Alansito", last_name="Rosete", email="alanroset3@gmail.com")
    rep.save()

    art1 = Article(headline="Lorem ipsum dolot", pub_date=date(2022,5,5), reporter=rep)
    art1.save()    
    art2 = Article(headline="Lorem set aimet", pub_date=date(2022,5,7), reporter=rep)
    art2.save() 

    result = art1.reporter.first_name

    return HttpResponse(result)
