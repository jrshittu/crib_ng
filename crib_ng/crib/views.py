from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def index(request):
    latest_product = Products.objects.order_by("-date_added")[:5]
    output = ", ".join([p.product_name for p in latest_product])
    return HttpResponse(output)

def detail(request, product_id):
    return HttpResponse('You\'re looking at product %s' %product_id)

def results(request, product_id):
    return HttpResponse("You're looking at the result of %s" %product_id)

def sale(request, product_id):
    return HttpResponse("You're looking at the number of sale of %s Houses" %product_id)


