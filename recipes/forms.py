from django import forms
from .models import Recipe


class RecipeModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(RecipeModelForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super(RecipeModelForm, self).save(*args, **kwargs)
        if self.request:
            obj.user = self.request.user
            obj.save()
        return obj

    class Meta:
        model = Recipe
        fields = [
            "title",
            "ingredients",
            "text",
            "pic",
        ]



