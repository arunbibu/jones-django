# Generated by Django 4.2.4 on 2023-09-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0010_blogs_excerpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='title', max_length=200, unique=True)),
            ],
        ),
    ]
