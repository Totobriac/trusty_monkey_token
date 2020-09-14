# Generated by Django 3.0.8 on 2020-08-15 09:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('maps', models.CharField(max_length=140, primary_key=True, serialize=False, unique=True)),
                ('adress', models.CharField(max_length=240)),
                ('lat', models.FloatField(default='0000000')),
                ('lng', models.FloatField(default='0000000')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('maps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Restaurant')),
                ('review_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StarterPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=40)),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('name_2', models.CharField(blank=True, max_length=40, null=True)),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('lat_pic_2', models.FloatField(blank=True, null=True)),
                ('lng_pic_2', models.FloatField(blank=True, null=True)),
                ('shot_time_2', models.DateTimeField(blank=True, null=True)),
                ('restaurant_review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview')),
            ],
            options={
                'verbose_name': 'StarterPics',
                'verbose_name_plural': 'StarterPics',
            },
        ),
        migrations.CreateModel(
            name='OutsidePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('restaurant_review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview')),
            ],
            options={
                'verbose_name': 'OutsidePics',
                'verbose_name_plural': 'OutsidePics',
            },
        ),
        migrations.CreateModel(
            name='MenuPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('lat_pic_2', models.FloatField(default='0000000')),
                ('lng_pic_2', models.FloatField(default='0000000')),
                ('shot_time_2', models.DateTimeField(default=datetime.datetime.now)),
                ('restaurant_review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview')),
            ],
            options={
                'verbose_name': 'MenuPics',
                'verbose_name_plural': 'MenuPics',
            },
        ),
        migrations.CreateModel(
            name='MainPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=40)),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('name_2', models.CharField(blank=True, max_length=40, null=True)),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('lat_pic_2', models.FloatField(blank=True, null=True)),
                ('lng_pic_2', models.FloatField(blank=True, null=True)),
                ('shot_time_2', models.DateTimeField(blank=True, null=True)),
                ('restaurant_review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview')),
            ],
            options={
                'verbose_name': 'MainPics',
                'verbose_name_plural': 'MainPics',
            },
        ),
        migrations.CreateModel(
            name='InsidePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('restaurant_review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview')),
            ],
            options={
                'verbose_name': 'InsidePics',
                'verbose_name_plural': 'InsidePics',
            },
        ),
        migrations.CreateModel(
            name='DessertPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=40)),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('name_2', models.CharField(blank=True, max_length=40, null=True)),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('lat_pic_2', models.FloatField(blank=True, null=True)),
                ('lng_pic_2', models.FloatField(blank=True, null=True)),
                ('shot_time_2', models.DateTimeField(blank=True, null=True)),
                ('restaurant_review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview')),
            ],
            options={
                'verbose_name': 'DessertPics',
                'verbose_name_plural': 'DessertPics',
            },
        ),
    ]
