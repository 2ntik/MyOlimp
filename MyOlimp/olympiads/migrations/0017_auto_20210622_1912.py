# Generated by Django 3.1.7 on 2021-06-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympiads', '0016_auto_20210428_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='olympiad',
            name='olympiad_url',
            field=models.CharField(blank='false', default='Ссылка не найдена =(', max_length=60, verbose_name='Ссылка на сайт олимпиады'),
        ),
    ]
