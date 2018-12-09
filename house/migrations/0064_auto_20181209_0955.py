# Generated by Django 2.1 on 2018-12-09 02:55

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0063_auto_20181208_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house_details',
            name='end_status',
        ),
        migrations.RemoveField(
            model_name='house_details',
            name='start_status',
        ),
        migrations.RemoveField(
            model_name='house_details',
            name='title',
        ),
        migrations.AddField(
            model_name='house_details',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=2016),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment_house',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 9, 55, 15, 484888)),
        ),
    ]
