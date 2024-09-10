from django.shortcuts import render, redirect, get_object_or_404
from main_app.forms import *
from django.db.models import Q


# Create your views here.
def index(request):
    banner = Banner.objects.all()
    product = Product.objects.all()
    category = Category.objects.all()

#Add to Cart counting
    cart_item_count = Cart.objects.count()

    # Pass the count to the template
  
    context ={
        'banner' : banner,
        'product' : product,
        'category' : category,
        'cart_item_count': cart_item_count,
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

#Cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity +=1
        cart_item.save()
    
    return redirect('/')

#Add to Cart Counting
def front_page(request):
    # Count all items added to the cart
    cart_item_count = Cart.objects.count()

    # Pass the count to the template
  
    context ={
        'cart_item_count': cart_item_count,
    }
    
    return render(request, 'mainapp/base.html', context)


