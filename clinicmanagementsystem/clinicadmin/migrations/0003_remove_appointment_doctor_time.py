# Generated by Django 3.2.6 on 2021-09-22 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicadmin', '0002_auto_20210919_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctor_time',
        ),
    ]