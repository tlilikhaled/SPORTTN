# Generated by Django 3.2.9 on 2021-12-06 22:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_shippingaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAddress',
            new_name='ShoppingAddress',
        ),
    ]
