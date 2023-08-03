from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render 
from .models import Products


# Create your views here.
def index(request):
    latest_product = Products.objects.order_by("-date_added")[:5]

    context = {
        "latest_product": latest_product,
    }

    return HttpResponse(render(request, "crib/index.html", context))


def detail(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    return render(request, "crib/detail.html", {"product", product})

def results(request, product_id):
    return HttpResponse("You're looking at the result of %s" %product_id)

def sale(request, product_id):
    return HttpResponse("You're looking at the number of sale of %s Houses" %product_id)


