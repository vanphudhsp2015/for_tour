# Generated by Django 2.1 on 2018-09-25 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_auto_20180924_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 25, 8, 54, 50, 184650)),
        ),
        migrations.AlterField(
            model_name='house_tour',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 25, 8, 54, 50, 185649)),
        ),
    ]