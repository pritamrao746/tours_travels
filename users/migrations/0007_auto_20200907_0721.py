# Generated by Django 3.1 on 2020-09-07 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userbookings_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookings',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
