# Generated by Django 3.2.11 on 2022-02-14 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0056_auto_20220214_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='upload_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 22, 2, 43, 208337)),
        ),
    ]
