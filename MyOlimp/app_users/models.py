from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from olympiads.models import OlympiadSubject


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Населённый пункт', default='Москва')

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название учебного заведения')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Населённый пункт')
    url = models.CharField(max_length=100, verbose_name='Сайт школы',
                           null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}, {self.city}'


class Profile(models.Model):
    SEX_CHOICES = [
        ('M', 'Мужской'),
        ('Ж', 'Женский'),
    ]
    GRADE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('У', 'Учитель')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='М',
                           verbose_name='Пол')
    third_name = models.CharField(max_length=30, verbose_name='Отчество')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default='1',
                             verbose_name='Класс обучения')
    age = models.PositiveSmallIntegerField(default=7, verbose_name='Возраст',
                                           validators=[
                                               MaxValueValidator(100),
                                               MinValueValidator(4)
                                           ]
                                           )
    school = models.ForeignKey(School, on_delete=models.PROTECT,
                               verbose_name='Учебное заведение',
                               blank=True, null=True, default=None)
    interest = models.ManyToManyField(OlympiadSubject,
                                      verbose_name='Интересующие предметы')
    personal_data = models.BooleanField(null=False, default=True,
                                        verbose_name='Галочка на согласие о работе с персональными данными')

    def get_absolute_url(self):
        return reverse('profile')

    def __str__(self):
        return f'{User.last_name} {User.first_name}, {self.grade}, {self.school}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
