from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *


def product(request):
    products=Products.objects.all()
    context={"products":products}
    return render(request,'products.html',context)
    
def product(request):
    products=Products.objects.all()
    if request.method=='POST':
        new_order=Orders()
        product_=request.POST.get('product')
        name_=request.POST.get('name')
        email_=request.POST.get('email')
        phone_=request.POST.get('phone')
        quantity_=request.POST.get('quantity')
        new_order=Orders(name=name_,email=email_,phone=phone_,quantity=quantity_,product=product_)
        new_order.save()

    context={"products":products}
    return render(request,'products.html',context)
            
              
    