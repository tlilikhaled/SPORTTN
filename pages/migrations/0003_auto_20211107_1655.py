# Generated by Django 3.2.8 on 2021-11-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20211105_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='contact@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(default='first name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(default='last name', max_length=100),
            preserve_default=False,
        ),
    ]
