# Generated by Django 2.1.4 on 2019-01-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20190101_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='num_of_rates',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10),
        ),
    ]
