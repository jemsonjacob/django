# Generated by Django 3.2.6 on 2021-09-27 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0003_timesheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.batch'),
        ),
    ]
