from django.core.mail import send_mail
from django.conf import settings


def send_email(subject, message):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER + '@yandex.ru',
        [settings.EMAIL_HOST_USER + '@ya.ru'],
        fail_silently=False,
    )
    return True
