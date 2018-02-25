from django import forms
# from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from .models import User

class RegisterForm(forms.Form):
    username = forms.CharField(
        label=_('Имя пользователя'),
        required=True,
    )
    email = forms.EmailField(
        label='Email',
        required=True
    )
    password1 = forms.CharField(
        label=_('Пароль'),
        required=True,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=_('Подтверждение пароля'),
        required=True,
        widget=forms.PasswordInput()
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                _('Пользователь с таким именем уже существует.')
            )

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                _('Пользователь с таким email уже существует.')
            )

        return email

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean().copy()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            self.add_error(None, _('Пароли не совпадают.'))

        return cleaned_data