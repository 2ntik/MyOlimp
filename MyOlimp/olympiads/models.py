from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class OlympiadSubjectGroup(models.Model):
    subject_group_name = models.CharField(max_length=40,
                                          verbose_name='Область',
                                          null=False)

    def __str__(self):
        return self.subject_group_name


class OlympiadSubject(models.Model):
    subject_name = models.CharField(max_length=30, verbose_name='Предмет', null=False)
    subject_group_name = models.ForeignKey(OlympiadSubjectGroup,
                                           on_delete=models.PROTECT,
                                           verbose_name='Направление')

    def __str__(self):
        return f'{self.subject_name}.' #Направление: {self.subject_group_name}'


class Olympiad(models.Model):
    LEVEL_CHOICES = [
        ('Всероссийская', 'Всероссийская'),
        ('Межрегиональная', 'Межрегиональная'),
        ('Региональная', 'Региональная'),
        ('Городская', 'Городская'),
        ('Школьная', 'Школьная'),
    ]
    title = models.CharField(max_length=100,
                             verbose_name='Название олимпиады',
                             null=False,
                             db_index=True)
    subject = models.ForeignKey(OlympiadSubject,
                                on_delete=models.PROTECT,
                                verbose_name='Предмет',
                                db_index=True)
    olympiad_level = models.CharField(max_length=20,
                                      choices=LEVEL_CHOICES,
                                      verbose_name='Уровень проведения олимпиады',
                                      default='Школьная')
    olympiad_extramural_start = models.DateField(blank=True,
                                                 verbose_name='Начало заочного тура',
                                                 default=None, null=True)
    olympiad_extramural_end = models.DateField(blank=True,
                                               verbose_name='Конец заочного тура',
                                               default=None,
                                               null=True)
    olympiad_intramural_start = models.DateField(blank=True,
                                                 verbose_name='Начало очного тура',
                                                 default=None,
                                                 null=True)
    olympiad_intramural_end = models.DateField(blank=True,
                                               verbose_name='Конец очного тура',
                                               default=None,
                                               null=True)
    olympiad_url = models.CharField(max_length=60,
                                    verbose_name='Ссылка на сайт олимпиады',
                                    default='Ссылка не найдена =(',
                                    null=False, blank='false')
    olympiad_file = models.FileField(blank=True, null=True,
                                     upload_to='static/model_files/',)
    winner = models.ForeignKey(User, on_delete=models.PROTECT,
                               verbose_name='Победитель',
                               blank=True, null=True,
                               default=None)
    participants = models.ManyToManyField(User, blank=True,
                                          verbose_name='Участники',
                                          related_name='+')

    def get_absolute_url(self):
        return reverse('olympiads')

    def __str__(self):
        return f'{self.name}, {self.olympiad_level}'
