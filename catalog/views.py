from django.shortcuts import render
from catalog.models import *
from django.views import generic

# Create your views here.

def index(request):

    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_instance = BookInstance.objects.count()

    #Availaible books with the status('a')
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()
    
    #Number of authors
    num_authors = Author.objects.count()
    #num_genre = Genre.objects.count()

    context = {

        'num_books': num_books, 
        'num_instance': num_instance,
        'num_instance_available': num_instance_available,
        'num_authors': num_authors,
    }

    return render(request, 'catalog/index.html', context)




class BookListView(generic.ListView):
    model = Book

    def get_context_data(self,**Kwargs):
        #call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**Kwargs)
        #Create any data and add it to the context
        context['book_list'] = Book.objects.all()
        return context

class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 2

class AuthorListView(generic.ListView):
    model = Author

    def get_context_data(self,**Kwargs):
        #call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**Kwargs)
        #Create any data and add it to the context
        context['author_list'] = Author.objects.all()
        return context

class AuthorDetailView(generic.DetailView):
    model = Author

