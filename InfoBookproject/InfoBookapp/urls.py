from django.urls import path

from . import views
from .views import BookList, BookCreate, BookInsert

app_name = 'teamapp'
urlpatterns = [
    path('', BookList.as_view(), name='index'),
    path('list/', BookList.as_view(), name='list'),
    path('create/', BookCreate.as_view(), name='create'),
    path('insert/', BookInsert.as_view(), name='insert'),
]