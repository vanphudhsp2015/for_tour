# Generated by Django 2.1 on 2018-12-07 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0051_auto_20181207_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 19, 57, 15, 452521)),
        ),
    ]