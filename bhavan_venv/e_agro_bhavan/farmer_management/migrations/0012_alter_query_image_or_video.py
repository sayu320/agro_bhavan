# Generated by Django 4.2.2 on 2023-07-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_management', '0011_alter_query_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='image_or_video',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
