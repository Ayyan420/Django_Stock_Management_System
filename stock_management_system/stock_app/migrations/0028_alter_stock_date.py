# Generated by Django 3.2.11 on 2022-02-10 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0027_stock_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 22, 31, 36, 774210)),
        ),
    ]
