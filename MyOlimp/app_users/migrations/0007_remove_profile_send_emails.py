# Generated by Django 3.2.4 on 2021-06-23 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0006_auto_20210622_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='send_emails',
        ),
    ]
