# Generated by Django 3.2.11 on 2022-02-13 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0046_auto_20220213_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='created_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 16, 26, 27, 307890)),
        ),
    ]