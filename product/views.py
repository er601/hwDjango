from django.shortcuts import render, HttpResponse
from .models import Category


# Create your views here.
def homepage(request):
    categories = Category.objects.all()
    context = {'all_categories': categories}
    return render(request, 'categories.html', context)
