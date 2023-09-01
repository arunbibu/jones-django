import uuid
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

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
    
class TagManager(models.Model):
    meta_tag = models.TextField()
    other_contet = models.TextField()
