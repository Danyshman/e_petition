# Generated by Django 2.1.4 on 2019-01-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20181230_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='average_rate',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10),
        ),
    ]
