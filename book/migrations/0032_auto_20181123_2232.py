# Generated by Django 2.1 on 2018-11-23 15:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0031_auto_20181123_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album_tour',
            name='date_up',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 668690)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 665692)),
        ),
        migrations.AlterField(
            model_name='book_tour',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 665692)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 667691)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 667691)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 666692)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 666692)),
        ),
        migrations.AlterField(
            model_name='place_tour',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Place'),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 665692)),
        ),
        migrations.AlterField(
            model_name='restaurant_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 665692)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_book',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 666692)),
        ),
        migrations.AlterField(
            model_name='vehicle_tour',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 22, 32, 18, 666692)),
        ),
    ]