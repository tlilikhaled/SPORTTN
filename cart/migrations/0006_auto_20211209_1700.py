# Generated by Django 3.2.9 on 2021-12-09 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_shoppingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingaddress',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='shoppingaddress',
            name='order',
        ),
    ]
