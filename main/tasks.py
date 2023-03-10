import logging
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from quick_publisher.celery import app


@app.task
def send_verification_email(user_id):

    UserModel = get_user_model()

    try:

        user = UserModel.objects.get(pk=user_id)

        send_mail(
            'Проверка верефикации',
            'Пожалуйста пройдите по ссылке: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            'skkqw@yandex.ru',
            [user.email],
            fail_silently=False,
        )

    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
