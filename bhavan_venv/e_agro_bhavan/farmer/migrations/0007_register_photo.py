# Generated by Django 4.2.2 on 2023-08-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0006_register_aadhar_register_panchayath_register_ward'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
