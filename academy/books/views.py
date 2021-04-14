from django.shortcuts import render
from .models import BookModel

def book_list(request):
    books = BookModel.objects.all()
    context = {'books':books}

    return render(request, 'books/books.html', context)