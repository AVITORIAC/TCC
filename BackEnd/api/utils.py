from django.core.mail import EmailMessage
from meinung import settings

# função para envio de email da nova senha
def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER, # verificar como faz isso
        to=[data['to_email']]
    )
    email.send()