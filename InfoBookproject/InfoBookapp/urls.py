from django.urls import path

from . import views
from .views import BookList, BookDetail, BookCreate, BookInsert

app_name = 'teamapp'
urlpatterns = [
    path('list/', BookList.as_view(), name='list'),
    path('detail/', BookDetail.as_view(), name='detail'),
    path('create/', BookCreate.as_view(), name='create'),
    path('insert/', BookInsert.as_view(), name='insert'),
]