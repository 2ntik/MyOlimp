# Generated by Django 3.1.7 on 2021-04-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympiads', '0014_auto_20210425_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olympiad',
            name='olympiad_level',
            field=models.CharField(choices=[('Всероссийская', 'Всероссийская'), ('Межрегиональная', 'Межрегиональная'), ('Региональная', 'Региональная'), ('Городскоая', 'Городскоая'), ('Школьная', 'Школьная')], default='Школьная', max_length=20, verbose_name='Уровень проведения олимпиады'),
        ),
    ]