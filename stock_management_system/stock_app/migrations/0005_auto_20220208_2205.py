# Generated by Django 3.2.11 on 2022-02-08 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0004_auto_20220208_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
