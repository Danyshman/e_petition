# Generated by Django 2.1.4 on 2019-02-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('road', 'Жолдор/Дороги'), ('street_lights', 'Уличное освещение'), ('gardening', 'Жашылдандыруу/Озеленение'), ('electricity', 'Элект камсыздоо/Электроснабжение'), ('water', 'Водоснабжение'), ('rubbish', 'Таштанды/Мусор'), ('heat', 'Жылуулук/Теплоснабжение'), ('other', 'Башка/Другое')], max_length=100),
        ),
    ]
