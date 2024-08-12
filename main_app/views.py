from django.shortcuts import render, redirect
from main_app.forms import Contactform, Banner


# Create your views here.
def index(request):
    banner = Banner.objects.all()

    context ={
        'banner' : banner,
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
