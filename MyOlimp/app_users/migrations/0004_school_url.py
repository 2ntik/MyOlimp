# Generated by Django 3.1.7 on 2021-04-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_auto_20210422_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='url',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Сайт школы'),
        ),
    ]
