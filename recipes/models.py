from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from django.contrib.auth import models as auth_models
from core import models as core_models
from core.models import NULL_BLANK


class Recipe(core_models.TimeStampable, core_models.Publishable):

    title = models.CharField(
        verbose_name=_('Название рецепта'),
        max_length=100,
        default='Title'
    )

    ingredients = models.TextField(verbose_name=_('Ингридиенты'), **NULL_BLANK)

    text = models.TextField(verbose_name=_('Инструкция'), **NULL_BLANK)

    pic = models.FileField(
        verbose_name=_('Картинка'),
        upload_to='.',
        **NULL_BLANK
    )
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Рецепт')
        verbose_name_plural = _('Рецепты')
        ordering = ['-date_created', '-date_updated']


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.TextField()
    quantity = models.FloatField()
    unit = models.TextField()


class Review(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    review_text = models.TextField()
