# Generated by Django 4.2.2 on 2023-08-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer_management', '0017_scheme_description_scheme_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
