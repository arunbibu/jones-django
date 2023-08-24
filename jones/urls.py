from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('listing/', views.listing, name='listing'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('property-single/', views.property_single, name='property-single'),
]