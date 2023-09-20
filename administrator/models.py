import uuid
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import User

from django_resized import ResizedImageField
from django.utils.text import slugify


class CustomUser(AbstractUser):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)


class HomeHeroBanner(models.Model):
    def thumb_upload(instance, filename):
        return 'home/hero-banner/{0}/{1}'.format(slugify(instance.heading), filename)
    heading = models.CharField(default="heading", max_length=255)
    tagline = models.CharField(default="tagline", max_length=255)
    image = ResizedImageField(upload_to=thumb_upload,
                              force_format="WEBP", quality=100, blank=True)
    slug = models.CharField(default="slug", max_length=255)
    button = models.CharField(default="button", max_length=255)


class Testimonials(models.Model):
    def thumb_upload(instance, filename):
        return 'testimonial/{0}/{1}'.format(slugify(instance.name), filename)

    name = models.CharField(default="name", max_length=255)
    designation = models.CharField(default="designation", max_length=255)
    image = ResizedImageField(upload_to=thumb_upload,
                              force_format="WEBP", quality=100, blank=True)
    content = models.TextField(
        default="Lorem Ipsum is simply dummy text of the printing and typesetting industry.")

    def __str__(self):
        return (self.name)


class Blogs(models.Model):
    cat = (
        ("article", "Articles"),
        ("blogs", "Blogs"),
        ("news", "News")
    )

    def thumb_upload(instance, filename):
        return 'blogs/{0}/{1}'.format(slugify(instance.title), filename)
    category = models.CharField(max_length=20, choices=cat, default='blogs')
    title = models.CharField(max_length=200, unique=True,
                             blank=True, default="title")
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, default="title")
    content = models.TextField()
    thumb = ResizedImageField(upload_to=thumb_upload,
                              force_format="WEBP", quality=100, blank=True)
    excerpt = models.TextField(blank=True)
    created_on = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class FilterParent(models.Model):
    title = models.CharField(max_length=200, unique=True,
                             blank=True, default="title")


class Filter(models.Model):
    parent = models.ForeignKey(FilterParent, on_delete=models.CASCADE)
    value = models.CharField(max_length=50, blank=True, default="value")

# contact form

class ContactForm(models.Model):
    REQUIREMENTS_CHOICES = [
        ('find_property', 'Find a Property'),
        ('list_property', 'List a Property'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    requirements = models.CharField(max_length=20, choices=REQUIREMENTS_CHOICES)
    message = models.TextField()
    created_on = models.DateField(default=timezone.now)



class TagManager(models.Model):
    meta_tag = models.TextField()
    other_contet = models.TextField()
