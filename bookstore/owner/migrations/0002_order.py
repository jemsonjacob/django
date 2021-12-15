# Generated by Django 3.2.6 on 2021-09-02 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('delivered', 'delivered'), ('cancelled', 'cancelled'), ('in transist', 'in transist')], default='ordered', max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('expected_delivery', models.DateField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.book')),
            ],
        ),
    ]