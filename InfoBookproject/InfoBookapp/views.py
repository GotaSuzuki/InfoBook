from django.shortcuts import render
from .models import BookInfo
from django.views.generic import ListView, DetailView, CreateView

class BookList(ListView):
    template_name = 'list.html'
    model = BookInfo

class BookDetail(DetailView):
    template_name = 'detali.html'
    model = BookInfo

class BookCreate(CreateView):
    template_name = 'create.html'
    model = BookInfo

class BookInsert(DetailView):
    template_name = 'insert.html'
    model = BookInfo