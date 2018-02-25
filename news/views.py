import logging
log = logging.getLogger(__name__)

from django.http import Http404, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from . import models, forms


class NewsList(ListView):
    model = models.News
    template_name = 'news/news_list.html'

    def get(self, request, *args, **kwargs):
        log.info("New list called!")
        return super().get(request, *args, **kwargs)


class NewsCreate(CreateView):
    model = models.News
    form_class = forms.NewsCreate
    template_name = 'news/news_create.html'
    success_url = reverse_lazy('news:list')


class NewsDetail(DetailView):
    model = models.News
    template_name = 'news/news_detail.html'


class NewsUpdate(UpdateView):
    model = models.News
    template_name = 'news/news_update.html'
    success_url = reverse_lazy('news:list')
    form_class = forms.NewsUpdate


class NewsDelete(DeleteView):
    model = models.News
    success_url = reverse_lazy('news:list')