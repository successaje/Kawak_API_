from django.urls import path

from .views import (
    EssayCreateAPIView,
    EssayDeleteAPIView,
    EssayDetailAPIView,
    EssayListAPIView

)

urlpatterns = [
    path('', EssayListAPIView.as_view(), name = "essays"),
    path('<int:id>', EssayDetailAPIView.as_view(), name = "essay-detail"),
    path('<int:id>/create', EssayCreateAPIView.as_view(), name='create-essay'),
    path('<int:id>/delete', EssayDeleteAPIView.as_view(), name = 'delete-essay'),
]
