from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView, TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='recipes/header.html'), name='header'),
    #path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('ru/register/', views.register, name='register'),
    path('my_recipes/', views.recipes, name='recipes'),
    path('newrecipe/', views.RecipeCreateView.as_view(), name='new_recipe'),
    path('my_recipes/detail/<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
