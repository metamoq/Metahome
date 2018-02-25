from django import forms

from . import models


class NewsCreate(forms.ModelForm):

    class Meta:
        model = models.News
        fields = [
            'title',
            'preview',
            'body'
        ]
        # exclude = ['id']


class NewsUpdate(forms.ModelForm):

    class Meta:
        model = models.News
        fields = [
            'title',
            'preview',
            'body'
        ]