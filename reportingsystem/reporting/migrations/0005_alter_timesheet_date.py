# Generated by Django 3.2.6 on 2021-09-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_alter_timesheet_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
