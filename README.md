# Ex02 Django ORM Web Application
## Date: 05:03:2024

## AIM
To develop a Django appl
pythonication to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](<Screenshot 2024-03-05 110716.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

models.py
```
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

admin.py

from django.contrib import admin
from .models import book_DB,book_DBAdmin
admin.site.register(book_DB,book_DBAdmin)
```


## OUTPUT
![alt text](<Screenshot 2024-03-04 144245.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
