from django.urls import path
from .views import BookListCreateView, BookDetailView,AllBooksListView,BookDeleteView,BookUpdateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/all/', AllBooksListView.as_view(), name='all-books-list'),  
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'), 
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'), 
]
