from django.urls import path
from . import fn_views
from . import views
urlpatterns = [
    path('', fn_views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>', views.BookDelete.as_view(), name='book-delete'),
    path('catalog/authors/', views.AuthorsListView.as_view(), name='authors-list'),
    path('catalog/author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowedbooks/', views.LoanedBooksLibrarianListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', fn_views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]
