from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from urllib.parse import urljoin


def send_verify_mail(user):
    verify_link = reverse(
        'auth:verify',
        args=[user.email, user.activation_key]
        )
    subject = 'Подтвердите учетную запись'
    massage = f"""
        Для подтверждения учетной записи {user.username} на портале
    {settings.DOMAIN_NAME} перейдите по ссылке: {urljoin(settings.DOMAIN_NAME, verify_link)}
    """
    send_mail(subject, massage, 'noreply@localhost', [user.email])