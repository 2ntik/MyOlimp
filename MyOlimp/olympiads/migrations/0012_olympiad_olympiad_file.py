# Generated by Django 3.1.7 on 2021-04-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympiads', '0011_auto_20210419_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='olympiad',
            name='olympiad_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
