# Generated by Django 3.0.5 on 2020-04-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaLS', '0003_auto_20200422_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, to='instaLS.Like'),
        ),
    ]
