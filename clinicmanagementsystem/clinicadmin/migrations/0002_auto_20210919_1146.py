# Generated by Django 3.2.6 on 2021-09-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='image',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_fee',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_time',
            field=models.PositiveIntegerField(),
        ),
    ]
