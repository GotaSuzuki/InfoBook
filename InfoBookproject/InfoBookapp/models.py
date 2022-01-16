from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField

class BookInfo(models.Model):
    title = CharField(help_text='書籍名', max_length=30)
    author = CharField(help_text='著者名', max_length=30)
    yomigana = CharField(help_text='読み仮名', max_length=30)
    company = CharField(help_text='出版社', max_length=30)
    date = DateField(help_text='出版日')
    page = IntegerField(help_text='ページ数')
    chance = CharField(help_text='購入のきっかけ', max_length=100)
    overview = TextField(help_text='概要')

    def __str__(self):
        return self.title