from django import forms
from django.db.models import fields
from django.shortcuts import redirect, render

from news.forms import ArticlesForm
from .models import Artiles
from django.views.generic import DetailView,UpdateView,DeleteView

def news_home(request):
    news = Artiles.objects.all()
    return render(request,'news/news_home.html',{'news':news})

class ArtilesDetailView(DetailView):
    model = Artiles  # Указываем модель
    template_name = 'news/article_detail.html'  # Шаблон для отображения
    form_class = ArticlesForm
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Artiles  # Указываем модель
    template_name = 'news/create.html'  # Шаблон для отображения
    form_class = ArticlesForm
    context_object_name = 'article'

class NewsDeleteView(DeleteView):
    model = Artiles  # Указываем модель
    success_url = '/news/'
    template_name = 'news/news-delete.html'  # Шаблон для отображения
    context_object_name = 'article'



def create(request):
    error = ''
    if request.method == 'POST':
        form  = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не правильна'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)