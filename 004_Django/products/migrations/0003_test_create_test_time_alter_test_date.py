# Generated by Django 4.0.6 on 2022-07-24 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_test_alter_product_options_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='create',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
