# Generated by Django 4.2.4 on 2023-09-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_homeherobanner_button'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('blogs', 'Blogs'), ('news', 'News')], default='1', max_length=20)),
            ],
        ),
    ]