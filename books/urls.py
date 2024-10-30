from django.urls import path
from . import views

urlpatterns = [
    path('v1/books/', views.list_book, name='list-book'),  # List all books
    path('v1/book/<uuid:pk>/', views.get_book, name='get-book'),  # Retrieve a book by ID
    path('v1/book/', views.create_book, name='create-book'),  # Create a new book
    path('v1/books/<uuid:pk>/', views.update_book, name='update-book'),  # Update a book
    path('v1/book/<uuid:pk>', views.delete_book, name='delete-book'),  # Delete a book
]
