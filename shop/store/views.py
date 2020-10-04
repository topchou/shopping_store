from django.shortcuts import render
from django.http import HttpResponse 
from .models import Product 
from django.template import loader

def index(request):
    latest_product_list = Product.objects.order_by('-create_date')[:5]
    context ={'latest_product_list': latest_product_list}
    return render(request, 'store/index.html', context)


def products(request, product_id):
    return HttpResponse("You are looking at %s" %product_id)