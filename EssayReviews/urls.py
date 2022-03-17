from django.urls import path

from . import views

urlpatterns = [
    path('', views.EssayReviewListAPIView.as_view(), name = "essays reviews"),
    path('<int:id>', views.EssayReviewDetailAPIView.as_view(), name = "essay reviews"),
]
