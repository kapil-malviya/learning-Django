from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

# Create your views here.


'''
def info_view(request):
	books = Book.objects.all()
	return render(request, 'testapp/info.html', {'books':books})
'''


class BookListView(ListView):
	model = Book
	# default template file for this : book_list.html          (: modelname_list.html
	# default context object : book_list
	# template_name = 'testapp/books.html'
	# context_object_name = 'list_of_books'



class BookDetailView(DetailView):
	model = Book
	# default template file for this : book_detail.html
	# default context object : book or book_detail