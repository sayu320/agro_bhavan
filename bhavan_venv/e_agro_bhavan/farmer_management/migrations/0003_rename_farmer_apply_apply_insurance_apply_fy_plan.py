# Generated by Django 4.2.2 on 2023-07-17 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0006_register_aadhar_register_panchayath_register_ward'),
        ('farmer_management', '0002_alter_farmer_apply_date_on_which_crop_failure_occured'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Farmer_apply',
            new_name='Apply_Insurance',
        ),
        migrations.CreateModel(
            name='Apply_FY_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_no', models.IntegerField(default='', max_length=50)),
                ('scheme_name', models.CharField(default='', max_length=50)),
                ('house_no', models.IntegerField(default='', max_length=50)),
                ('age_of_the_applicant', models.IntegerField(default='', max_length=50)),
                ('ration_card_no', models.IntegerField(default='', max_length=50)),
                ('category', models.CharField(choices=[('Minority', 'Minority'), ('Others', 'Others')], default='Minority', max_length=250, verbose_name='CATEGORY')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farmer.register')),
            ],
        ),
    ]
