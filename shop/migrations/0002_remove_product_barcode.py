# Generated by Django 3.0.6 on 2020-06-10 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='barcode',
        ),
    ]
