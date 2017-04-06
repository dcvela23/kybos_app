# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terrarium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('price_small', models.DecimalField(decimal_places=2, max_digits=100)),
                ('price_medium', models.DecimalField(decimal_places=2, max_digits=100)),
                ('price_big', models.DecimalField(decimal_places=2, max_digits=100)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('B', 'Big')], default=1, max_length=1)),
                ('colors', models.CharField(choices=[('S', 'Silver'), ('M', 'Bronce'), ('B', 'Black')], default=1, max_length=1)),
                ('cover', models.ImageField(upload_to='images')),
                ('cover_main', models.ImageField(upload_to='images')),
                ('img_one', models.ImageField(upload_to='images')),
                ('img_two', models.ImageField(upload_to='images')),
                ('img_three', models.ImageField(upload_to='images')),
                ('img_four', models.ImageField(upload_to='images')),
            ],
        ),
    ]
