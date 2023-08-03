from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello welcome to my site")

def detail(request, product_id):
    return HttpResponse('You\'re looking at product %s' %product_id)

def results(request, product_id):
    return HttpResponse("You're looking at the result of %s" %product_id)

def sale(request, product_id):
    return HttpResponse("You're looking at the number of sale of %s" %product_id)


