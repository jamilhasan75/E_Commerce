from main_app.models import Category, Cart, Wishlist

def g_categories(request):
    g_category = Category.objects.all()
    return {'g_category': g_category}

def g_cart(request):
    card = Cart.objects.count()
    return {'card': card}

def g_wishlist(request):
    wishlist = Wishlist.objects.count()
    return {'wishlist': wishlist}