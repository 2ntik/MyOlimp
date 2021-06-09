# Generated by Django 3.1.7 on 2021-04-08 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OlympiadLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Уровень проведения олимпиады')),
            ],
        ),
        migrations.CreateModel(
            name='OlympiadRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Тур')),
            ],
        ),
        migrations.CreateModel(
            name='OlympiadSubjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_group_name', models.CharField(max_length=40, verbose_name='Область')),
            ],
        ),
        migrations.CreateModel(
            name='OlympiadSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=30, verbose_name='Предмет')),
                ('subject_group_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='olympiads.olympiadsubjectgroup', verbose_name='Направление')),
            ],
        ),
        migrations.CreateModel(
            name='Olympiad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название олимпиады')),
                ('olympiad_round_time_start', models.DateTimeField(null=True, verbose_name='Начало очного тура')),
                ('olympiad_round_time_end', models.DateTimeField(verbose_name='Конец очного тура')),
                ('olympiad_round_not_real_time_start', models.DateTimeField(null=True, verbose_name='Начало заочного тура')),
                ('olympiad_round_not_real_time_end', models.DateTimeField(verbose_name='Конец заочного тура')),
                ('olympiad_round', models.ForeignKey(default='Очный тур', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='olympiad_round', to='olympiads.olympiadround')),
                ('olympiad_round_not_real', models.ForeignKey(default='Заочный тур', null=True, on_delete=django.db.models.deletion.PROTECT, to='olympiads.olympiadround')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='olympiads.olympiadsubject', verbose_name='Предмет')),
            ],
        ),
    ]
