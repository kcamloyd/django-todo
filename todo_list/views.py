from django.shortcuts import render
from .models import List

def home(request):
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

def about(request):
    context = {'first_name': 'Katie', 'last_name': 'Loyd'}
    return render(request, 'about.html', context)