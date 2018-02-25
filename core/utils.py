from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _


def send_activation_email(profile, host):
    import time
    send_mail(
        _('Регистрация'),
        _(
            'Вы зарегистрировались на сайте. '
            'Ссылка для активации:'
        ) + ' {url}'.format(
            url='http://' + host + '/' + profile.activation.url
        ),
        from_email='test@test.by',
        recipient_list=[profile.email],
        fail_silently=False
    )