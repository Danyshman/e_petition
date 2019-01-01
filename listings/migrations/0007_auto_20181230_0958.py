# Generated by Django 2.1.4 on 2018-12-30 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20181227_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='closed_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='listing',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'В ожидании'), ('in_process', 'В процессе'), ('completed', 'Закрыто')], default='pending', max_length=200),
        ),
    ]
