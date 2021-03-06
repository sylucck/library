from django.urls import path, include
from catalog import views

urlpatterns = [

     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
     path('books/<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),
     path('author/', views.AuthorListView.as_view(), name='authors'),
     path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
     path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
     path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    
    
]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
]


# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]

# Add URLConf to create, update, and delete books
urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<slug:slug>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<slug:slug>/delete/', views.BookDelete.as_view(), name='book-delete'),
]