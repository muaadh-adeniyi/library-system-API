from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from books.views import home

# Create the schema view for Swagger
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

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('', home, name='home'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
