# Generated by Django 2.1 on 2018-09-20 12:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tourer', '0007_remove_tourer_time_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_house',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commnet', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 9, 20, 19, 53, 35, 949895))),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourer.Tourer')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_house', models.CharField(max_length=250)),
                ('type_house', models.CharField(max_length=250)),
                ('image_house', models.FileField(default='/default/user-avatar-default-165.png', upload_to='house/')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.City')),
            ],
        ),
        migrations.CreateModel(
            name='House_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('start_status', models.CharField(max_length=5000)),
                ('end_status', models.CharField(max_length=5000)),
                ('img_status', models.FileField(default='/default/user-avatar-default-165.png', upload_to='house/book/')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.House')),
            ],
        ),
        migrations.CreateModel(
            name='House_tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 9, 20, 19, 53, 35, 950893))),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourer.Tourer')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.House')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=250)),
                ('price', models.FloatField(default=0)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.House')),
            ],
        ),
        migrations.AddField(
            model_name='comment_house',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.House'),
        ),
    ]
