from django.shortcuts import render, redirect
from main_app.forms import *
from django.db.models import Q


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
#Related product show
    related_products = Product.objects.filter(category=productd.category).exclude(id=productd.pk).order_by('?')[:11]

    context ={
        'product' : productd,
        'related_products' : related_products,
    }
    return render(request, 'mainapp/product.html', context)

#Search
def product_search(request):
    query = request.GET['q']
    lookup = (
        Q(name__icontains=query) |
        Q(category__c_name__icontains=query) | 
        Q(brand__name__icontains=query)
        )
    search_product = Product.objects.filter(lookup)

    context = {
        'search_product': search_product
    }
    return render(request,'mainapp/product_search.html',context)

#Category product show
def categories_product(request, pk):
    filtering = Category.objects.get(pk=pk)
    product_filter = Product.objects.filter(category=filtering.id)
    return render(request, 'mainapp/categories_product.html', {'product_filter': product_filter})


#About us page
def about(request):
    return render(request, 'mainapp/about.html')


