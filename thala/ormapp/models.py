from django.db import models
from django.contrib import admin
class book_DB(models.Model):
    bookno=models. IntegerField(primary_key="bookno")
    bookname=models.CharField(max_length=20)
    author=models.CharField(max_length=30)
    pageno=models.IntegerField()
    language=models.CharField(max_length=30)
class book_DBAdmin(admin.ModelAdmin):
    list_display=("bookno", "bookname","author", "pageno","language");