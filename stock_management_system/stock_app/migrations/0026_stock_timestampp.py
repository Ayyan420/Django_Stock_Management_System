# Generated by Django 3.2.11 on 2022-02-10 22:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0025_remove_stock_export_to_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='timestampp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
