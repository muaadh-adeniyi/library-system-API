from  .serializers import BookSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from django.http import Http404
from  django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect


# Create your views here.

# List all books
@api_view(['GET'])
def list_book(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    data = {
        "status" : "success",
        "code" : status.HTTP_200_OK,
        "message" : "Books retrieved successfully",
        "data" : {
            "books" : serializer.data
        }
    }
    return Response(data , status= status.HTTP_200_OK)

# Retrieve book by id
@api_view(['GET'])
def get_book(request , pk):
    try:
         books = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return Response ({
            "status" : "error",
            "code" : 404,
            "message" : "Book not found",
            "errors" : {
                "details" : f"No book found with id {pk}"
            }
        }, status= status.HTTP_404_NOT_FOUND )

    serializer = BookSerializer(books)
    data = {
        "status" : "success",
        "code" : status.HTTP_200_OK,
        "message" : "Book retrieved successfully",
        "data" : serializer.data
    }
    return Response(data , status= status.HTTP_200_OK)


# Add new book
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
        return Response(data, status=status.HTTP_201_CREATED )

    data = {
        "status": "error",
        "code": status.HTTP_400_BAD_REQUEST,
        "message": "Book creation failed",
        "errors": serializer.errors
    }
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


# update a book
@api_view(['PUT'])
def update_book(request , pk):
    try:
        book = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return Response({
            "status" : "error",
            "code" : 404,
            "message" : "book not found",
            "errors" : {
                "details" : f"No book found with id{pk}."
            }
,        } , status= status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book  , data= request.data)
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


# delete a book
@api_view(['DELETE'])
def delete_book(request , pk):
    try:
        books = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return Response({
            "status" : "error",
            "code" : 404 ,
            "message" : "",
            "errors" : {
                "details" : f"No book found with id {pk}."
            }
        } , status= status.HTTP_404_NOT_FOUND)

    books.delete()
    return Response({
        "status": "success",
        "code" : status.HTTP_204_NO_CONTENT ,
        "message" : "Book deleted successfully",
        "data" : None
    } , status= status.HTTP_204_NO_CONTENT)




schema_view = get_schema_view(
    openapi.Info(
        title="Library System API",
        default_version='v1',
        description="API documentation for the Library System",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="muaadhadeleye@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def home(request):
    # Redirect to Swagger documentation
    return redirect('schema-swagger-ui')












        


