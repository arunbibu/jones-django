from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('find-a-property/', views.listing, name='listing'),
    path('about-jones-asset-management/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('jones-interiors/', views.interiors, name='interiors'),
    path('service/', views.service, name='service'),
    path('property-single/', views.property_single, name='property-single'),
    path('list-a-property/', views.properties, name='properties'),
    path('thank-you/', views.thank_you, name='thank-you'),
    path('real-estate-guide/', views.real_estate_guide, name='real-estate-guide'),
    path('real-estate-guide/<slug:slug>/', views.real_estate_guide_single, name='real-estate-guide-single'),
]