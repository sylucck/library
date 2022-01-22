from django.urls import path, include
from catalog import views

urlpatterns = [

     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
     path('books/<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),
     path('author/', views.AuthorListView.as_view(), name='authors'),
     path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail')
    
]