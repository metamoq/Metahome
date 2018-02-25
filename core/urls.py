from django.contrib.auth.views import logout_then_login, logout, login
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.urls import path

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='core/homepage.html'
    ), name='index'),
    path('Информация', TemplateView.as_view(
        template_name='core/about.html'
    ), name='about'),
    path('about/',views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.RegisterView.as_view(), name='ok_register'),
    path('activate/<str:token>/', views.ActivateView.as_view(), name='activate'),
    path('login/', login, {'template_name': 'core/login.html'}, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', views.profile, name='personal'),
    path('news/', include(('news.urls', 'news'), namespace='news')),
]
