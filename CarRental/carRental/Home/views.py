from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.http import HttpResponseRedirect
from .models import *
from Shop.models import *
from Rental.models import *


def home(request):
    marks = Mark.objects.all()
    context = {"marks":marks}
    return render(request, 'home.html', context)

def searchvenues(request):
    car = Car.objects.all()
    product = Products.objects.all()
    if request.method == "POST":
        searched = request.POST.get('search')
        if searched:
            venues = Car.objects.filter(car_name__contains=searched)
            pro = Products.objects.filter(product_name__contains=searched)
            if venues or pro :
                context={'searched':searched,'venues':venues,'car':car, 'product':product , 'pro':pro}
                return render(request,'search.html',context)
            else:
                messages.info(request, ' ')
        else:   
            return HttpResponseRedirect('/search/')
    context={'venues':venues,'car':car, 'product':product , 'pro':pro}
    return render(request,'search.html',context)