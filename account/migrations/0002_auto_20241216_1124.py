# Generated by Django 3.0.7 on 2024-12-16 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('D', 'Doctor'), ('P', 'Patient'), ('R', 'Receptionist'), ('HR', 'HR'), ('CH', 'Consultant')], max_length=2),
        ),
    ]
