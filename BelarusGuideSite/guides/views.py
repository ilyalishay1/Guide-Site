from django.shortcuts import render


def home(request):
    return render(request, 'guides/home.html')


def destinations(request):
    return render(request, 'guides/destinations.html')


def activities(request):
    return render(request, 'guides/activities.html')


def about_us(request):
    return render(request, 'guides/about_us.html')


def minsk(request):
    return render(request, 'guides/minsk.html')


def grodno(request):
    return render(request, 'guides/grodno.html')


def brest(request):
    return render(request, 'guides/brest.html')
