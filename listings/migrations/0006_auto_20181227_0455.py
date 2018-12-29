# Generated by Django 2.1.4 on 2018-12-27 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20181226_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='photo_1',
            new_name='photo_description_1',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='photo_2',
            new_name='photo_description_2',
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_result_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_result_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
