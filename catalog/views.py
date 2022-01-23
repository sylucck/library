from django.shortcuts import render
from catalog.models import *
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):

    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_instance = BookInstance.objects.count()

    #Availaible books with the status('a')
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()
    
    #Number of authors
    num_authors = Author.objects.count()
    #num_genre = Genre.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {

        'num_books': num_books, 
        'num_instance': num_instance,
        'num_instance_available': num_instance_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'catalog/index.html', context)

#checking if browser supports cookies
def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response

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


from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_borrowed_users.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')