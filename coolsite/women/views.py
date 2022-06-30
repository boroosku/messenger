from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import *
from .models import *
from .utils import *

def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
    }

    return render(request, 'women/index.html', context=context)

def addpage(request):
    cur_user = request.user
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                d = form.cleaned_data
                d['author'] = cur_user.id
                Women.objects.create(**d)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        #c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()))

    def form_valid(self, form):
        user1 = form.save()
        profile = Profile(user=user1)
        profile.save()
        login(self.request, user1)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        #c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')