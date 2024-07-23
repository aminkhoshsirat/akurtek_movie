from django.core.mail import send_mail


def send_activation_code(email, code):
    send_mail(
        subject='Akurtek Movie Activation Code',
        message=f'http://localhost:8000/activation/{code}',
        from_email=email
    )

