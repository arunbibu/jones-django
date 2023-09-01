from django.shortcuts import render
from django.http import HttpResponse
from administrator.models import HomeHeroBanner, Testimonials


# home view


def home(request):
    banners = HomeHeroBanner.objects.all()
    testimonials = Testimonials.objects.all()
    return render(request, 'jones/home.html', {"banners": banners, "testimonials": testimonials})

# listing view


def listing(request):
    return render(request, 'jones/listing.html')


# about view

def about(request):
    return render(request, 'jones/about.html')


# property_single view

def property_single(request):
    return render(request, 'jones/property-single.html')

# lease or rent property


def properties(request):
    return render(request, 'jones/properties.html')


# real_estate_guide
def real_estate_guide(request):
    return render(request, 'jones/blog.html')

# real_estate_guide single


def real_estate_guide_single(request):
    return render(request, 'jones/blog-single.html')


# interiors
def interiors(request):
    return render(request, 'jones/interiors.html')

# leasing


def leasing(request):
    return render(request, 'jones/leasing.html')

# rental


def rental(request):
    return render(request, 'jones/rental.html')

# sell


def sell(request):
    return render(request, 'jones/sell.html')


# contact view

def contact(request):
    return render(request, 'jones/contact.html')
