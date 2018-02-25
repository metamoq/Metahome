from datetime import timedelta

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.utils.timezone import now
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, RedirectView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.db import transaction

from . import models, forms
from core import tasks


def about(request):
    return render(request, 'core/about.html')


def news(request):
    return render(request, 'news/news_list.html')


def index(request):
    return render(request, 'core/homepage.html')


def profile(request):
    return render(request, 'core/profile.html')


def contact(request):
    return render(request, 'core/contact.html', {'content': ['Телефон службы поддержки', '+375292369785', 'werewolf13@list.ru']})


class RegisterView(FormView):
    form_class = forms.RegisterForm
    template_name = 'core/register_form.html'
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():

            with transaction.atomic():
                try:
                    profile = models.Profile.objects.create(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password2'],
                        email=form.cleaned_data['email'],
                        is_active=False
                    )
                    profile.set_password(profile.password)
                    activation = models.Activation(
                        valid_until=now() + timedelta(minutes=2)
                    )
                    activation.set_url()
                    activation.save()
                    profile.activation = activation
                    profile.save()
                except Exception as exc:
                    messages.error(
                        request,
                        _('Не удалось создать учётную запись.'
                          )
                    )
                    raise exc
                else:
                    messages.success(
                        request,
                        _('Учётная запись была создана. '
                          'Сообщение со ссылкой для активации будет выслано '
                          'на Ваш email.'
                          )
                    )
                    # send_mail(subject, message, from_email, to_list, fail_silently=True)
                    subject = _('Подтверждение почты')
                    message = profile.username + ', вот ваша cсылка для активации:' + ' {url}'.format(
                                    url='http://' + self.request.META['HTTP_HOST'] + '/' + profile.activation.url
                                )
                    from_email = 'cookwiki@support.by'
                    to_list = [profile.email]
                    send_mail(subject, message, from_email, to_list, fail_silently=False)

            return self.form_valid(form)

        return self.form_invalid(form)


class ActivateView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        try:
            activation = models.Activation.objects.get(url__icontains=token)
        except models.Activation.DoesNotExist:
            messages.error(
                request,
                _('Не удалось активировать учётную запись.')
            )
            return redirect('register')

        activation.profile.is_active = True
        activation.profile.save()

        return super(ActivateView, self).get(request, *args, **kwargs)