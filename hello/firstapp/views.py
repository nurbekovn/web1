from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2> Main Page </h2>")

def about(request):
    return HttpResponse("<h2> About Site </h2>")

def contact(request):
    return HttpResponse("<h2> Contact </h2>")

def products(request, productId = 1):
    output = "<h2> Product № {0} </h2>".format(productId)
    return HttpResponse(output)

def users(request, id, name):
    output = "<h2> User </h2> <h3> id: {0} Name: {1} </h3>".format(id, name)
    return HttpResponse(output)

