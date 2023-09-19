from django.shortcuts import render
from django.http import HttpResponse
from administrator.models import HomeHeroBanner, Testimonials, Blogs, ContactForm


# home view


def home(request):
    banners = HomeHeroBanner.objects.all()
    testimonials = Testimonials.objects.all()
    blog = Blogs.objects.filter()
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
    type = request.GET.get('type')
    print(type)
    if type == "all":
        blog = Blogs.objects.filter()
    elif type:
        blog = Blogs.objects.filter(category=type)
    else:
        blog = Blogs.objects.filter()
    return render(request, 'jones/blog.html',{"blogs": blog})

# real_estate_guide single


def real_estate_guide_single(request,slug):
    blog = Blogs.objects.get(slug=slug)
    return render(request, 'jones/blog-single.html',{"blog":blog})


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
    if request.method == 'POST':
        name = request.POST.get('jones-name')
        email = request.POST.get('jones-email')
        phone = request.POST.get('jones-phone')
        requirements = request.POST.get('jones-requirements')
        message = request.POST.get('jones-message')
        
        if name and email and message:
            contacts = ContactForm(name=name,email=email,phone=phone,requirements=requirements,message=message)
            contacts.save()
        return render(request, 'jones/contact.html')
    if request.method == 'GET':
        return render(request, 'jones/contact.html')
