# Generated by Django 2.1 on 2018-10-03 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_auto_20181003_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 18, 56, 1, 556408)),
        ),
    ]
