# Generated by Django 2.1 on 2018-11-16 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0013_auto_20181116_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 16, 47, 59, 957933)),
        ),
    ]