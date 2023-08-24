from datetime import datetime
from django.contrib.auth import authenticate, login, logout  # type: ignore waning
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
# from slugify import slugify
from django.db import transaction
from django.db.models import Q
from django.contrib import messages

from administrator.models import *


# authentication


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(dashboard)
        else:
            messages.error(request, "Invalid Credentials")
            return redirect(login_user)
    if request.method == "GET":
        logout(request)
        return render(request, 'administrator/login.html')

# logout user


def logout_view(request):
    logout(request)
    return redirect(login_user)


# dashboard


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'administrator/dashboard.html')


# Hero Banner Section


@login_required(login_url='login')
def home_hero_banner(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            if request.user.has_perm('administrator.view_homeherobanner'):
                banners = HomeHeroBanner.objects.all()
                return render(request, 'administrator/home/hero-banner.html', {'banners': banners})
            else:
                return HttpResponse('This user is not Authorized to view Media Files')
        if request.method == "POST":
            heading = request.POST['banner-heading']
            tagline = request.POST['banner-tagline']
            slug = request.POST['banner-slug']
            image = request.FILES['banner-image']
            banner = HomeHeroBanner(
                heading=heading, tagline=tagline, slug=slug, image=image)
            banner.save()
            return redirect(home_hero_banner)
    else:
        return HttpResponse('Please Login first to view Media Files')


@login_required(login_url='login')
def home_hero_banner_list(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('administrator.view_homeherobanner'):
            if request.method == "GET":
                try:
                    banner = HomeHeroBanner.objects.filter(
                        id=id).values('id', 'heading', 'tagline', 'slug')
                    return JsonResponse({'result': list(banner)})
                except Exception as e:
                    print(str(e))
                    return JsonResponse({'result': False, 'content': 'Error Occured while listing the hero banner'})
            else:
                return JsonResponse({'result': False, 'content': 'Incorrect Method'})
        else:
            return JsonResponse({'result': 'This user is not Authorized to view hero banner'})
    else:
        return JsonResponse({'result': 'This user is not Authorized to view hero banner'})


@login_required(login_url='login')
def home_hero_banner_update(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('administrator.change_homeherobanner'):
            if request.method == "POST":
                try:
                    heading = request.POST['banner-heading']
                    tagline = request.POST['banner-tagline']
                    slug = request.POST['banner-slug']
                    banner = HomeHeroBanner.objects.get(id=id)
                    banner.heading = heading
                    banner.tagline = tagline
                    if request.FILES:
                        image = request.FILES['banner-image']
                        banner.image = image
                    banner.slug = slug
                    banner.save()
                    return redirect(home_hero_banner)
                except Exception as e:
                    print(str(e))
                    return HttpResponse('Error Occured while updating')
            else:
                return HttpResponse('Incorrect Method')
        else:
            return HttpResponse('This user is not Authorized to change hero banner')
    else:
        return HttpResponse('This user is not Authorized to change hero banner')


@login_required(login_url='login')
def home_hero_banner_delete(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('administrator.delete_homeherobanner'):
            if request.method == "POST":
                try:
                    banner = HomeHeroBanner.objects.get(id=id)
                    banner.delete()
                    return JsonResponse({'result': True})
                except:
                    return JsonResponse({'result': False, 'content': 'Error Occured while deleting'})
            else:
                return JsonResponse({'result': False, 'content': 'Incorrect Method'})
        else:
            return JsonResponse({'result': 'This user is not Authorized to delete hero banner'})
    else:
        return JsonResponse({'result': 'This user is not Authorized to delete hero banner'})
    

# Testimonials Section


@login_required(login_url='login')
def testimonials(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            if request.user.has_perm('administrator.view_testimonials'):
                testimonials = Testimonials.objects.all()
                return render(request, 'administrator/home/testimonials.html', {'testimonials': testimonials})
            else:
                return HttpResponse('This user is not Authorized to view Testimonials')
        if request.method == "POST":
            name = request.POST['testimonial-name']
            designation = request.POST['testimonial-designation']
            content = request.POST['testimonial-content']
            image = request.FILES['testimonial-image']
            testimonial = Testimonials(
                name=name, designation=designation, content=content, image=image)
            testimonial.save()
            return redirect("testimonial")
    else:
        return HttpResponse('Please Login first to view Testimonials')


@login_required(login_url='login')
def testimonials_list(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('administrator.view_testimonials'):
            if request.method == "GET":
                try:
                    testimonial = Testimonials.objects.filter(
                        id=id).values('id', 'name', 'designation', 'content')
                    return JsonResponse({'result': list(testimonial)})
                except Exception as e:
                    print(str(e))
                    return JsonResponse({'result': False, 'content': 'Error Occured while listing the testimonial'})
            else:
                return JsonResponse({'result': False, 'content': 'Incorrect Method'})
        else:
            return JsonResponse({'result': 'This user is not Authorized to view testimonial'})
    else:
        return JsonResponse({'result': 'This user is not Authorized to view testimonial'})


@login_required(login_url='login')
def testimonials_update(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('administrator.change_testimonials'):
            if request.method == "POST":
                try:
                    name = request.POST['testimonial-name']
                    designation = request.POST['testimonial-designation']
                    content = request.POST['testimonial-content']
                    testimonial = Testimonials.objects.get(id=id)
                    testimonial.name = name
                    testimonial.designation = designation
                    if request.FILES:
                        image = request.FILES['testimonial-image']
                        testimonial.image = image
                    testimonial.content = content
                    testimonial.save()
                    return redirect("testimonial")
                except Exception as e:
                    print(str(e))
                    return HttpResponse('Error Occured while updating')
            else:
                return HttpResponse('Incorrect Method')
        else:
            return HttpResponse('This user is not Authorized to change testimonial')
    else:
        return HttpResponse('This user is not Authorized to change testimonial')


@login_required(login_url='login')
def testimonials_delete(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('administrator.delete_testimonials'):
            if request.method == "POST":
                try:
                    testimonial = Testimonials.objects.get(id=id)
                    testimonial.delete()
                    return JsonResponse({'result': True})
                except:
                    return JsonResponse({'result': False, 'content': 'Error Occured while deleting'})
            else:
                return JsonResponse({'result': False, 'content': 'Incorrect Method'})
        else:
            return JsonResponse({'result': 'This user is not Authorized to delete testimonial'})
    else:
        return JsonResponse({'result': 'This user is not Authorized to delete testimonial'})