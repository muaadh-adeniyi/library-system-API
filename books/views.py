from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import redirect

# Swagger schema for list of books
@swagger_auto_schema(
    method="get",
    responses={200: openapi.Response("Books retrieved successfully", BookSerializer(many=True))}
)
@api_view(['GET'])
def list_book(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    data = {
        "status": "success",
        "code": status.HTTP_200_OK,
        "message": "Books retrieved successfully",
        "data": {
            "books": serializer.data
        }
    }
    return Response(data, status=status.HTTP_200_OK)


# Swagger schema for retrieving a book by ID
@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response("Book retrieved successfully", BookSerializer),
        404: "Book not found"
    },
    manual_parameters=[
        openapi.Parameter("pk", openapi.IN_PATH, description="ID of the book to retrieve", type=openapi.TYPE_STRING, format="uuid", required=True)
    ]
)
@api_view(['GET'])
def get_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({
            "status": "error",
            "code": 404,
            "message": "Book not found",
            "errors": {"details": f"No book found with id {pk}"}
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)
    data = {
        "status": "success",
        "code": status.HTTP_200_OK,
        "message": "Book retrieved successfully",
        "data": serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)


# Swagger schema for creating a new book
@swagger_auto_schema(
    method="post",
    request_body=BookSerializer,
    responses={
        201: openapi.Response("Book created successfully", BookSerializer),
        400: "Invalid data"
    }
)
@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            "status": "success",
            "code": status.HTTP_201_CREATED,
            "message": "Book created successfully",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)

    data = {
        "status": "error",
        "code": status.HTTP_400_BAD_REQUEST,
        "message": "Book creation failed",
        "errors": serializer.errors
    }
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


# Swagger schema for updating a book
@swagger_auto_schema(
    method="put",
    request_body=BookSerializer,
    responses={
        200: openapi.Response("Book updated successfully", BookSerializer),
        404: "Book not found",
        400: "Invalid data"
    },
    manual_parameters=[
        openapi.Parameter("pk", openapi.IN_PATH, description="ID of the book to update", type=openapi.TYPE_STRING, format="uuid", required=True)
    ]
)
@api_view(['PUT'])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({
            "status": "error",
            "code": 404,
            "message": "Book not found",
            "errors": {"details": f"No book found with id {pk}"}
        }, status=status.HTTP_404_NOT_FOUND)

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
    }, status=status.HTTP_400_BAD_REQUEST)


# Swagger schema for deleting a book
@swagger_auto_schema(
    method="delete",
    responses={
        204: "Book deleted successfully",
        404: "Book not found"
    },
    manual_parameters=[
        openapi.Parameter("pk", openapi.IN_PATH, description="ID of the book to delete", type=openapi.TYPE_STRING, format="uuid", required=True)
    ]
)
@api_view(['DELETE'])
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({
            "status": "error",
            "code": 404,
            "message": "Book not found",
            "errors": {"details": f"No book found with id {pk}"}
        }, status=status.HTTP_404_NOT_FOUND)

    book.delete()
    return Response({
        "status": "success",
        "code": status.HTTP_204_NO_CONTENT,
        "message": "Book deleted successfully",
        "data": None
    }, status=status.HTTP_204_NO_CONTENT)


# Redirect to Swagger documentation as the home page
def home(request):
    return redirect('schema-swagger-ui')
