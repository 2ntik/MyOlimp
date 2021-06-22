from . import models
from olympiads.models import Olympiad
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf.global_settings import DEFAULT_FROM_EMAIL


def email_sender(*args, **kwargs):
    for user in User.objects.all():
        profile = models.Profile(user=user.id)
        if profile.send_emails:
            text = '''
            Вы подписались на письма с напоминаниями об олимпиадах!
            По интересующим Вас темам мы нашли следующие олимпиады.
            '''
            reciever = user.email
            for i in profile.interest:
                text += 'По предмету "'
                text += i
                text += '": \n'
                for olympiad in Olympiad.objects.all():
                    if olympiad.subject == i:
                        text += '\n'
                        text += olympiad.title
                text += '\n'
            text += 'Зайдите на сайт, чтобы посмотреть детальную информацию о них.'

            send_mail(subject='Напоминаем Вам об олимпиадах',
                      message=text,
                      from_email=DEFAULT_FROM_EMAIL,
                      recipient_list=[reciever])
