# Generated by Django 3.0.8 on 2020-08-23 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20200817_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessertpic',
            name='lat_pic_2',
        ),
        migrations.RemoveField(
            model_name='dessertpic',
            name='lng_pic_2',
        ),
        migrations.RemoveField(
            model_name='dessertpic',
            name='name_2',
        ),
        migrations.RemoveField(
            model_name='dessertpic',
            name='picture_2',
        ),
        migrations.RemoveField(
            model_name='dessertpic',
            name='shot_time_2',
        ),
        migrations.RemoveField(
            model_name='mainpic',
            name='lat_pic_2',
        ),
        migrations.RemoveField(
            model_name='mainpic',
            name='lng_pic_2',
        ),
        migrations.RemoveField(
            model_name='mainpic',
            name='name_2',
        ),
        migrations.RemoveField(
            model_name='mainpic',
            name='picture_2',
        ),
        migrations.RemoveField(
            model_name='mainpic',
            name='shot_time_2',
        ),
        migrations.RemoveField(
            model_name='menupic',
            name='lat_pic_2',
        ),
        migrations.RemoveField(
            model_name='menupic',
            name='lng_pic_2',
        ),
        migrations.RemoveField(
            model_name='menupic',
            name='picture_2',
        ),
        migrations.RemoveField(
            model_name='menupic',
            name='shot_time_2',
        ),
        migrations.RemoveField(
            model_name='starterpic',
            name='lat_pic_2',
        ),
        migrations.RemoveField(
            model_name='starterpic',
            name='lng_pic_2',
        ),
        migrations.RemoveField(
            model_name='starterpic',
            name='name_2',
        ),
        migrations.RemoveField(
            model_name='starterpic',
            name='picture_2',
        ),
        migrations.RemoveField(
            model_name='starterpic',
            name='shot_time_2',
        ),
        migrations.AlterField(
            model_name='dessertpic',
            name='restaurant_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='insidepic',
            name='restaurant_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='mainpic',
            name='restaurant_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='menupic',
            name='restaurant_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='outsidepic',
            name='restaurant_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='starterpic',
            name='restaurant_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
    ]