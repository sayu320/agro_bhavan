# Generated by Django 4.2.2 on 2023-06-09 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farmer', '0002_rename_user_user_farmer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_farmer',
            name='uid',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
