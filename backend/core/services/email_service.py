import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.services.jwt_service import ActionToken, ActivateToken, JWTService


class EmailService:
    @classmethod
    def __send_email(cls, to: str, template_name: str, context: dict, subject: str) -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(
            to=[to],
            subject=subject,
            from_email=os.environ.get('EMAIL_HOST_USER')
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost/activate/{token}'
        cls.__send_email(
            to=user.email,
            template_name='register.html',
            context={'name': user.profile.name, 'url': url},
            subject="Register"
        )