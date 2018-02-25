from datetime import timedelta
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.test import TestCase, Client, RequestFactory

from recipes.models import Recipe

HTTP_OK_STATUS = 200
HTTP_NOT_FOUND_STATUS = 404
HTTP_FOUND_STATUS = 302


class UrlsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_wrong_url_return_http_NOT_FOUND_status(self):
        url = 'about/about/about/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_NOT_FOUND_STATUS, msg='Not OK')

    def test_default_url_return_http_302_status(self):
        url = ''
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_FOUND_STATUS, msg='Not OK')

    def test_ru_view_url_return_http_status(self):
        url = '/ru/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_login_view_url_return_http_status(self):
        url = '/ru/login/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_register_view_url_return_http_status(self):
        url = '/ru/register/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_logout_view_url_return_http_status(self):
        url = '/ru/recipes/logout'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 301, msg='Not OK')

    def test_about_view_url_return_http_status(self):
        url = '/ru/about/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_contact_view_url_return_http_status(self):
        url = '/ru/contact/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_news_list_view_url_return_http_status(self):
        url = '/ru/news/list/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_profile_view_url_return_http_status(self):
        url = '/ru/recipes/my_recipes/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302, msg='Not OK')

    def test_create_recipe_view_url_return_http_status(self):
        url = '/ru/recipes/newrecipe/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')
        
        
class RecipeCreateTest(TestCase):
    
    def test_recipe_recipe(self):
        user = User.objects.create_user(username='test', is_active=True, password='1234')
        recipe = Recipe(
            title='Pizza',
            ingredients='Muka, sol, sahar, yaica, kolbasa, tomatnaya pasta i sir.',
            text='vse smeshat i kinut v pech',
            owner=User.objects.get(username='test'))
        recipe.save()
        our_recipe = Recipe.objects.get(title='Pizza')
        self.assertEqual(str(recipe), recipe.title)
        self.assertEqual(our_recipe.title, recipe.title)
        self.assertEqual(our_recipe.ingredients, recipe.ingredients)
        self.assertEqual(our_recipe.owner, user)
        self.assertEqual(our_recipe.text, recipe.text)



