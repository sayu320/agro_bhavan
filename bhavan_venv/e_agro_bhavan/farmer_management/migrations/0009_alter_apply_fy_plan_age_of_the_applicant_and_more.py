# Generated by Django 4.2.2 on 2023-07-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_management', '0008_alter_apply_fy_plan_age_of_the_house_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_fy_plan',
            name='age_of_the_applicant',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apply_fy_plan',
            name='annual_income',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apply_fy_plan',
            name='house_no',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apply_fy_plan',
            name='ration_card_no',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apply_fy_plan',
            name='wasteland',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=250, verbose_name='Wasteland'),
        ),
    ]
