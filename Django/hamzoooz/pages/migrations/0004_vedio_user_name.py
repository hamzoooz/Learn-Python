# Generated by Django 4.0.6 on 2022-07-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_products_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('watch', models.ManyToManyField(null=True, to='pages.vedio')),
            ],
        ),
    ]