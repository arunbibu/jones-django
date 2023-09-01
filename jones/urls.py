from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.listing, name='listing'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('interiors/', views.interiors, name='interiors'),
    path('leasing/', views.leasing, name='leasing'),
    path('rental/', views.rental, name='rental'),
    path('sell/', views.sell, name='sell'),
    path('property-single/', views.property_single, name='property-single'),
    path('list-a-property/', views.properties, name='properties'),
    path('real-estate-guide/', views.real_estate_guide, name='real-estate-guide'),
    path('real-estate-guide-single/', views.real_estate_guide_single, name='real-estate-guide-single'),
]