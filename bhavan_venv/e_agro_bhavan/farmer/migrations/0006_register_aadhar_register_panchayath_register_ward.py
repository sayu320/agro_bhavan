# Generated by Django 4.2.2 on 2023-07-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0005_rename_user_farmer_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='aadhar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='register',
            name='panchayath',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='register',
            name='ward',
            field=models.IntegerField(default=0),
        ),
    ]
