# Generated by Django 4.2.2 on 2023-06-19 06:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farmer', '0004_user_farmer_location_user_farmer_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_farmer',
            new_name='Register',
        ),
    ]
