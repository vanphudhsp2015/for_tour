# Generated by Django 2.1 on 2018-12-07 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0052_auto_20181207_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 21, 24, 5, 781774)),
        ),
    ]
