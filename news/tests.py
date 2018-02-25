from django.test import TestCase, Client
from django.urls import reverse

from . import models


HTTP_OK_STATUS = 200
HTTP_NOT_FOUND_STATUS = 404
HTTP_REDIRECT_STATUS = 302


class UrlsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_wrong_url_return_http_NOT_FOUND_status(self):
        url = '/news/mew'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_NOT_FOUND_STATUS, msg='Not OK')

    def test_list_return_http_OK_status(self):
        url = reverse('news:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_detail_return_http_OK_status(self):
        news = models.News.objects.create()
        url = reverse('news:detail', kwargs={'pk': news.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_wrong_detail_id_return_http_NOT_FOUND_status(self):
        url = reverse('news:detail', kwargs={'pk': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_NOT_FOUND_STATUS, msg='Not OK')

    def test_delete_return_http_REDIRECT_status(self):
        news = models.News.objects.create()
        url = reverse('news:delete', kwargs={'pk': news.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, HTTP_REDIRECT_STATUS, msg='Not OK')


class TestNewsModels(TestCase):
    model = models.News

    def test_create(self):
        preview = 'Preview'
        body = 'Body'
        news = self.model.objects.create(preview=preview, body=body)
        self.assertEqual(news.preview, preview)
        self.assertEqual(news.body, body)
