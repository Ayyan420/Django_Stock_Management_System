# Generated by Django 3.2.11 on 2022-02-12 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0032_auto_20220212_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 12, 21, 58, 25, 646627)),
        ),
        migrations.AlterField(
            model_name='stocklisthistory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 12, 21, 58, 25, 647742), null=True),
        ),
    ]