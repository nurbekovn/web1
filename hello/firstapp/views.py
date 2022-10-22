from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect


def index(request):
    return HttpResponse("Index")


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponse("/about")

def details(request) :
    return HttpResponsePermanentRedirect("/")


def products(request, productId):
    category = request.GET.get("cat", "")
    output = "<h2> Product № {0} Category: {1} </h2>".format(productId, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Nurbekov")
    output = "<h2> User </h2> <h3> id: {0} Name: {1} </h3>".format(id, name)
    return HttpResponse(output)
