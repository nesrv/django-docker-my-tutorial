from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from selfedu.forms import AddUserForm
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_user'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


# menu = ['About', 'Add door', 'Add user', 'Login', 'Support']


# заменил функцию индекс классом HomePage
class HomePage(ListView):
    model = Employees
    template_name = 'selfedu/index.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['door_selected'] = 0
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Employees.objects.filter(is_active=True)

class UserDoorShow(ListView):
    model = Employees
    template_name = 'selfedu/index.html'
    context_object_name = 'users'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Users from : ' + str(context['users'][0].door)
        context['door_selected'] = context['users'][0].door_id
        context['menu'] = menu
        context['doors'] = Doors
        return context
    def get_queryset(self):
        return Employees.objects.filter(door__slug=self.kwargs['door_slug'])


class ShowUserInfo(DetailView):
    model = Employees
    template_name = 'selfedu/info.html'
    slug_url_kwarg = 'info_slug'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User info'
        context['menu'] = menu
        return context


class AddUser(CreateView):
    form_class = AddUserForm
    template_name = 'selfedu/adduser.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add user'
        context['menu'] = menu
        return context



def about(request):
    return render(request, 'selfedu/about.html', {'menu': menu, 'title': "About"})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")








def pageNotFound(request, exception):
    # здесь можно сделать запись в базу ошибок 301, 302, 500, 403, 400
    # handler500 - ошибка сервера
    # 403 - доступ запрещен
    # 400 - невозможно обработать запрос
    # 301 страница перемещена на другой url
    # 302 перемещена временно на другоq url

    return HttpResponseNotFound("<h1> No page </h1>")
