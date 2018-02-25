import os
import binascii

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from solo.models import SingletonModel


NULL_BLANK = {
    'null': True,
    'blank': True
}
NULL = {
    'null': True,
    'blank': False
}


class PublishableQueryset(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)

    def unpublished(self):
        return self.filter(is_published=False)


class PublishableManager(models.Manager):
    def get_queryset(self):
        return PublishableQueryset(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def unpublished(self):
        return self.get_queryset().unpublished()


class TimeStampable(models.Model):
    date_created = models.DateTimeField(
        default=now
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        **NULL_BLANK
    )

    class Meta:
        abstract = True


class Publishable(models.Model):
    is_published = models.BooleanField(
        default=False
    )

    objects = PublishableManager()

    class Meta:
        abstract = True


def get_profile_image_path(instance, filename):
    return '{username}/{filename}'.format(
        username=instance.user.username,
        filename=filename
    )


# class CustomUser(AbstractUser):
#     USERNAME_FIELD = 'email'

# class Profile2(models.Model):
#     user = models.OneToOneField(to=User, on_delete=models.CASCADE)
#     avatar = models.ImageField(
#         verbose_name=_('Аватар'),
#         upload_to=get_profile_image_path,
#         **NULL_BLANK
#     )

class SiteSettings(SingletonModel):
    activation_url_preiod = models.SmallIntegerField(
        verbose_name=_('Время действия ссылки, ч'),
        default=100
    )
    default_user_image = models.ImageField(
        verbose_name=_('Аватар по-умолчанию'),
        **NULL_BLANK
    )

    class Meta:
        verbose_name = ('Настройки сайта')


class Activation(models.Model):
    valid_until = models.DateTimeField(
        verbose_name=_('Ссылка активна до'),
    )
    url = models.URLField(
        verbose_name=_('Ссылка'),
    )

    def set_url(self):
        self.url = 'activate/{token}/'.format(
            token=binascii.hexlify(os.urandom(10)).decode('utf-8')
        )
        pass


class Profile(User):
    avatar = models.ImageField(
        verbose_name=_('Аватар'),
        upload_to=get_profile_image_path,
        **NULL_BLANK
    )
    activation = models.OneToOneField(
        verbose_name=_('Активация'),
        to=Activation,
        on_delete=models.SET_NULL,
        **NULL_BLANK
    )

class Follow(models.Model):
    id          = models.BigAutoField(primary_key=True)
    following_pk = models.IntegerField()
    user_pk     = models.IntegerField()
    create_time = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.following_pk) + " follows " + str(self.user_pk)

    def __unicode__(self):
        return str(self.following_pk) + " follows " + str(self.user_pk)