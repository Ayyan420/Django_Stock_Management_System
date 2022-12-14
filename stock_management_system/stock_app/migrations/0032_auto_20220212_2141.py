# Generated by Django 3.2.11 on 2022-02-12 21:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0031_alter_stock_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 12, 21, 41, 3, 683802)),
        ),
        migrations.CreateModel(
            name='StockListHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('receive_by', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('issue_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_to', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('receive_quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.IntegerField(blank=True, default=0, null=True)),
                ('issue_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default=0, null=True)),
                ('last_update', models.DateTimeField(null=True)),
                ('timestampp', models.DateTimeField(null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 2, 12, 21, 41, 3, 684827), null=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stock_app.categorie')),
            ],
        ),
    ]
