# Generated by Django 2.1 on 2018-11-16 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0016_auto_20181116_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 52, 25, 237652)),
        ),
    ]
