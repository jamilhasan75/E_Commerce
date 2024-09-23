from django.shortcuts import render
from main_app.models import *

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'dashboard/products/product_list.html', {'products': products})