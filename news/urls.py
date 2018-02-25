from django.urls import path
from django.views.generic import ListView, DetailView

from news import models
from . import views

urlpatterns = [
    path('list/', views.NewsList.as_view(), name='list'),
    path('create/', views.NewsCreate.as_view(), name='create'),
    path('update/<int:pk>', views.NewsUpdate.as_view(), name='update'),
    path('detail/<int:pk>', views.NewsDetail.as_view(), name='detail'),
    path('delete/<int:pk>', views.NewsDelete.as_view(), name='delete'),
    path('', ListView.as_view(model=models.News), name='news_list')
]