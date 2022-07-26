from django.shortcuts import render, HttpResponse
from .models import Category, Price


# Create your views here.
def all_categories(request):
    categories = Category.objects.all()
    context = {'all_categories': categories}
    return render(request, 'product/categories.html', context)


def pricing_table(request):
    price = Price.objects.all()
    context = {'pricing_table': price}
    return render(request, 'product/pricing_table.html', context)


def homepage(request):
    return render(request, 'homepage.html')

