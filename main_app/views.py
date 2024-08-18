from django.shortcuts import render, redirect
from main_app.forms import *


# Create your views here.
def index(request):
    banner = Banner.objects.all()
    product = Product.objects.all()
    category = Category.objects.all()

    context ={
        'banner' : banner,
        'product' : product,
        'category' : category,
    }

    return render (request, 'mainapp/index.html', context)

def contact(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = Contactform()
    return render(request, 'mainapp/contact.html',{'form':form})

#product details page
def product_detail(request, pk):
    productd = Product.objects.get(pk=pk)

    context ={
        'product' : productd,
    }
    return render(request, 'mainapp/product.html', context)
