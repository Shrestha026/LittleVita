# Generated by Django 5.0.2 on 2024-03-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0007_alter_vaccine_efficacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='date_of_approval',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='dosage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
