# Generated by Django 4.2.2 on 2023-07-04 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officer_management', '0003_alter_sub_scheme_s_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_scheme',
            name='s_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='officer_management.scheme'),
        ),
    ]
