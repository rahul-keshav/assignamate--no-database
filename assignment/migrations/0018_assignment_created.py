# Generated by Django 2.0.1 on 2018-06-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0017_blog_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]
