# Generated by Django 3.2.11 on 2022-02-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0011_auto_20220209_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_name',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
