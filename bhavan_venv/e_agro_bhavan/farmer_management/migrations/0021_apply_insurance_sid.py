# Generated by Django 4.2.2 on 2023-08-08 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officer_management', '0013_alter_products_price'),
        ('farmer_management', '0020_apply_state_horticulture_mission_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply_insurance',
            name='sid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='officer_management.sub_scheme'),
        ),
    ]
