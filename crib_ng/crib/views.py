from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render 
from .models import Products
from django.http import Http404

# Create your views here.
def index(request):
    latest_product = Products.objects.order_by("-date_added")[:5]

    context = {
        "latest_product": latest_product,
    }

    return HttpResponse(render(request, "crib/index.html", context))


def detail(request, product_id):
    try:
        product = Products.objects.get(pk=product_id)

    except Products.DoesNotExist:
        raise Http404("Product does not exist")
    
    return render(request, "crib/index.html", {"product": product})

def results(request, product_id):
    return HttpResponse("You're looking at the result of %s" %product_id)

def sale(request, product_id):
    return HttpResponse("You're looking at the number of sale of %s Houses" %product_id)


