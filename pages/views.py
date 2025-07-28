from django.views.generic import TemplateView
from django.views import View
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 50},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 2000},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 3000},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 4000}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'
    def get(self, request, id):
        # Activity 4
        try:
            product = Product.products[int(id)-1]
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse('home'))
            
        viewData = {}
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    # Activity 7
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("The price must be greater than 0")
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('product_created')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

# Activity 1
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact - Online Store",
            "subtitle": "Contact",
            "email": "contact@automatch.com",
            "address": "Carrera 36 # 62 - 45, Medellín, Colombia",
            "phone_number": "+57 300 123 4567"
        })
        return context

# Activity 8
class ProductCreatedView(View):
    template_name = 'products/product_created.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Product created - Online Store"
        viewData["subtitle"] = "A Laravel EAFIT App"
        return render(request, self.template_name, viewData)