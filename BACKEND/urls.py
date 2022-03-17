#BACKEND URL Configuration

from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Kawak API",
      default_version='v1',
      description="A Backend API for Kawak",
      terms_of_service="https://www.Kawak.com/policies/terms/",
      contact=openapi.Contact(email="contact@kawak.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('essays/', include('Essay.urls')),
    path('essays/reviews/', include('EssayReviews.urls')),
    path('contact-us/', include('contacts.urls')),
    path('waiting-list/', include('main.urls')),
    #path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
