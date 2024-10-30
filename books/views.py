from rest_framework import status
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import redirect

# List all books
@swagger_auto_schema(method='get', responses={200: BookSerializer(many=True)})
@api_view(['GET'])
def list_book(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({
        "status": "success",
        "code": status.HTTP_200_OK,
        "message": "Books retrieved successfully",
        "data": {"books": serializer.data}
    })

# Retrieve book by id
@swagger_auto_schema(method='get', responses={200: BookSerializer})
@api_view(['GET'])
def get_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({
            "status": "error",
            "code": status.HTTP_404_NOT_FOUND,
            "message": "Book not found",
            "errors": {"details": f"No book found with id {pk}"}
        })
    serializer = BookSerializer(book)
    return Response({
        "status": "success",
        "code": status.HTTP_200_OK,
        "message": "Book retrieved successfully",
        "data": serializer.data
    })

# Add new book (POST with auto-generated ID)
@swagger_auto_schema(
    method='post',
    request_body=BookSerializer,
    responses={201: BookSerializer}
)
@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # ID is auto-generated
        return Response({
            "status": "success",
            "code": status.HTTP_201_CREATED,
            "message": "Book created successfully",
            "data": serializer.data
        })
    return Response({
        "status": "error",
        "code": status.HTTP_400_BAD_REQUEST,
        "message": "Book creation failed",
        "errors": serializer.errors
    })

# Update a book
@swagger_auto_schema(
    method='put',
    request_body=BookSerializer,
    responses={200: BookSerializer}
)
@api_view(['PUT'])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({
            "status": "error",
            "code": status.HTTP_404_NOT_FOUND,
            "message": "Book not found",
            "errors": {"details": f"No book found with id {pk}"}
        })
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "Book updated successfully",
            "data": serializer.data
        })
    return Response({
        "status": "error",
        "code": status.HTTP_400_BAD_REQUEST,
        "message": "Book update failed",
        "errors": serializer.errors
    })

# Delete a book
@swagger_auto_schema(method='delete', responses={204: 'No Content'})
@api_view(['DELETE'])
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({
            "status": "error",
            "code": status.HTTP_404_NOT_FOUND,
            "message": "Book not found",
            "errors": {"details": f"No book found with id {pk}"}
        })
    book.delete()
    return Response({
        "status": "success",
        "code": status.HTTP_204_NO_CONTENT,
        "message": "Book deleted successfully",
        "data": None
    })

# Redirect to Swagger documentation on homepage
def home(request):
    return redirect('schema-swagger-ui')
