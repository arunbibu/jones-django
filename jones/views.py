from django.shortcuts import render
from django.http import HttpResponse
from administrator.models import HomeHeroBanner,Testimonials


# home view


def home(request):
    banners = HomeHeroBanner.objects.all()
    testimonials = Testimonials.objects.all()
    return render(request, 'jones/home.html', {"banners": banners,"testimonials":testimonials})

# listing view


def listing(request):
    return render(request, 'jones/listing.html')


# about view

def about(request):
    return render(request, 'jones/about.html')


# property_single view

def property_single(request):
    return render(request, 'jones/property-single.html')


# contact view

def contact(request):
    return render(request, 'jones/contact.html')
