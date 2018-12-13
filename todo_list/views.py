from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    context = {'first_name': 'Katie', 'last_name': 'Loyd'}
    return render(request, 'about.html', context)