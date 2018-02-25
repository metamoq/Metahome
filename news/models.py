from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import ugettext as _

from core import models as core_models
from core.models import NULL_BLANK


class News(
    core_models.TimeStampable,
    core_models.Publishable
):
    title = models.CharField(verbose_name=_('Название'),
        max_length=100,
        default='Title'
    )
    author = models.ForeignKey(
        verbose_name=_('Автор'),
        to=auth_models.User,
        **NULL_BLANK,
        on_delete=models.SET_NULL
    )
    preview = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')
        ordering = ['-date_created', '-date_updated']