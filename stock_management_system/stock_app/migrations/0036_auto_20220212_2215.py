# Generated by Django 3.2.11 on 2022-02-12 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0035_auto_20220212_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 12, 22, 15, 45, 13454)),
        ),
        migrations.AlterField(
            model_name='stocklisthistory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 12, 22, 15, 45, 14756), null=True),
        ),
    ]
