from django.urls import path, include

from .views import Contact_UsAPIView

urlpatterns = [
    path('', Contact_UsAPIView.as_view(), name = 'contact-us'),
]