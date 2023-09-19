# Generated by Django 4.2.4 on 2023-09-18 11:46

import administrator.models
import datetime
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_blogs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='blogs',
            name='content',
            field=models.TextField(default=datetime.date(2023, 9, 18)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='created_on',
            field=models.DateField(default=datetime.date(2023, 9, 18)),
        ),
        migrations.AddField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(blank=True, default='title', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='thumb',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to=administrator.models.Blogs.thumb_upload),
        ),
        migrations.AddField(
            model_name='blogs',
            name='title',
            field=models.CharField(blank=True, default='title', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='category',
            field=models.CharField(choices=[('blogs', 'Blogs'), ('news', 'News')], default='blogs', max_length=20),
        ),
    ]
