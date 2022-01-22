from django.shortcuts import render
from catalog.models import *
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





