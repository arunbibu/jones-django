from django.urls import path
from . import views


urlpatterns = [
    # login user
    path('', views.login_user, name='login'),
    # logout user
    path('logout/', views.logout_view, name='logout'),
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # hero-banner
    path('home/hero-banner/', views.home_hero_banner, name='home-hero-banner'),
    path('home/hero-banner/<int:id>/list/',
         views.home_hero_banner_list, name='home-hero-banner-list'),
    path('home/hero-banner/<int:id>/update/',
         views.home_hero_banner_update, name='home-hero-banner-update'),
    path('home/hero-banner/<int:id>/delete/',
         views.home_hero_banner_delete, name='home-hero-banner-delete'),
    # meta tag
    path('meta-tags/', views.meta_tags, name='meta-tags'),


    # testimonials
    path('home/testimonial/', views.testimonials, name='testimonial'),
    path('home/testimonial/<int:id>/list/',
         views.testimonials_list, name='testimonial-list'),
    path('home/testimonial/<int:id>/update/',
         views.testimonials_update, name='testimonial-update'),
    path('home/testimonial/<int:id>/delete/',
         views.testimonials_delete, name='testimonial-delete'),


    # blogs
    path('blog/', views.blogs, name='blog'),
    path('blog/<int:id>/list/',
         views.blogs_list, name='blog-list'),
    path('blog/<int:id>/update/',
         views.blogs_update, name='blog-update'),
    path('blog/<int:id>/delete/',
         views.blogs_delete, name='blog-delete'),
     #contact 
     path('contact/',views.contact,name="contact-list") 
    # properties
#     path('blog/', views.blogs, name='blog'),
#     path('blog/<int:id>/list/',
#          views.blogs_list, name='blog-list'),
#     path('blog/<int:id>/update/',
#          views.blogs_update, name='blog-update'),
#     path('blog/<int:id>/delete/',
#          views.blogs_delete, name='blog-delete'),
]
