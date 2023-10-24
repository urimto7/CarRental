from django.core.checks import messages
from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.

from django.http import HttpResponseRedirect


def rentpage(request):
    car = Car.objects.all
    if request.method=="POST" and 'subscribe' in request.POST:   
       email = request.POST['email']
       ins = Subscribes(subscribe_email=email)
       ins.save()
    context = {'car':car}
    return render(request , 'rentpage.html',context)

def rrs(request, id):
   car = Car.objects.get(car_id=id)
   image = Image.objects.filter(image_car=car)
   if request.method=="POST" and 'book' in request.POST: 
      new_book= Book()  
      book = request.POST.get('book')
      book1 = request.POST.get('book1')
      book2 = request.POST.get('book2')
      book3 = request.POST.get('book3')
      new_book=Book(BookNow_pick=book, BookNow_dropoff=book1,BookNow_datep=book2,BookNow_dated=book3)
      new_book.save()
      messages.success(request, 'Book request submitted successfully.')
   if request.method=="POST" and 'subscribe' in request.POST:   
       email = request.POST['email']
       ins = Subscribes(subscribe_email=email)
       ins.save()
   context = {'car':car,'image':image}
   return render(request,'rrs.html',context)

