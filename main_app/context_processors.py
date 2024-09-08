from main_app.models import Category

def g_categories(request):
    g_category = Category.objects.all()
    return {'g_category': g_category}