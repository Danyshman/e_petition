# Generated by Django 2.1.4 on 2018-12-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20181226_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(),
        ),
    ]
