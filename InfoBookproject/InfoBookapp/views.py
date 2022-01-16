from django.shortcuts import render
from .models import BookInfo
from django.views.generic import ListView, DetailView, CreateView

class BookIndex(ListView):
    template_name = 'index.html'
    model = BookInfo

class BookList(ListView):
    template_name = 'list.html'
    model = BookInfo

class BookCreate(CreateView):
    template_name = 'create.html'
    model = BookInfo

class BookInsert(DetailView):
    template_name = 'insert.html'
    model = BookInfo