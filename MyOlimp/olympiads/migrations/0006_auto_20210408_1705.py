# Generated by Django 3.1.7 on 2021-04-08 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympiads', '0005_auto_20210408_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='olympiad',
            old_name='olympiad_level',
            new_name='olympiad_level_id',
        ),
    ]