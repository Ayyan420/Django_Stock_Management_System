# Generated by Django 3.2.11 on 2022-02-10 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0026_stock_timestampp'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
            preserve_default=False,
        ),
    ]