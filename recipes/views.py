from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, DetailView
import logging

from core.models import Profile
from recipes.forms import RecipeModelForm
from recipes.models import Recipe

log = logging.getLogger(__name__)
from recipes import models
from news.models import News


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next = request.POST['next']
            if next != '':
                return render(request, next[1:] + '.html')
            else:
                return render(request, 'recipes/login_success.html')
        else:
            return render(request, 'recipes/login.html',
                          {'username': username, 'message': 'Неверное имя пользвателя либо пароль',
                           'next': request.POST['next']})

    if request.method == 'GET':
        if 'next' in request.GET:
            return render(request, 'recipes/login.html',
                          {'next': request.GET['next'], 'message': 'Эта страница требует вход'})
        else:
            return render(request, 'recipes/login.html')


def logout_page(request):
    logout(request)
    return render(request, 'recipes/logout.html')


@login_required
def recipes(request):
    context = {'my_recipes': Recipe.objects.filter(owner=request.user)}
    return render(request, 'recipes/recipes.html', context)


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeModelForm
    template_name = 'recipes/new_recipe.html'
    success_url = reverse_lazy('recipes')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            if request.user is not None:
                recipe = Recipe()
                recipe.title = form.cleaned_data['title']
                recipe.ingredients = form.cleaned_data['ingredients']
                recipe.text = form.cleaned_data['text']
                recipe.owner = User.objects.get(username=request.user)
                recipe.is_published = True
                recipe.pic = form.cleaned_data['pic']
                recipe.save()
                try:
                    form.save()
                except Exception:
                    pass
                # profile = Profile.objects.filter(user=User.objects.get(username=request.user))
                # profile.update(avatar=form.cleaned_data['avatar'])
                return super(RecipeCreateView, self).form_valid(form)
            else:
                return self.form_invalid(form)


class RecipeDetailView(DetailView):

    model = Recipe
    template_name = 'recipes/detail_recipe.html'


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, 'recipes/register.html',
                          {'message': 'Username ' + username + ' already taken', 'first_name': first_name,
                           'last_name': last_name, 'email': email})
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'recipes/register.html', {'message': 'Вы успешно зарегестрировались!'})

    if request.method == 'GET':
        return render(request, 'recipes/register.html')


class RecipeList(ListView):
    model = models.Recipe
    template_name = 'recipes/recipes.html'

    def get(self, request, *args, **kwargs):
        log.info("Recipe list called!")
        return super().get(request, *args, **kwargs)


