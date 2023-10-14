from urllib import request
from django.db import models
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . models import Product
from . forms import CustomerRegistrationForm
from django.contrib import messages
# Create your views here.
def sayHello(request):
    return render(request,'HelloWorld_App/home.html')

def about(request):
    return render(request,'HelloWorld_App/about.html')

def contact(request):
    return render(request,'HelloWorld_App/contact.html')

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,'HelloWorld_App/category.html',locals())

class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,'HelloWorld_App/category.html',locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'HelloWorld_App/productdetail.html',locals())


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'HelloWorld_App/customerregistraion.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulations! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'HelloWorld_App/customerregistraion.html',locals())