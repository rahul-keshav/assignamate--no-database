# Generated by Django 2.0.1 on 2018-07-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment_answered_by',
            name='assigner_username',
            field=models.CharField(max_length=150),
        ),
    ]
