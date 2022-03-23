from django.urls import path

from .views import (
    EssayReviewListAPIView,
    EssayReviewDetailAPIView,
    EssayReviewCreateAPIView
)

urlpatterns = [
    path('', EssayReviewListAPIView.as_view(), name = 'essay-reviews-list'),
    path('create/', EssayReviewCreateAPIView.as_view(), name = 'essay-reviews-create'),
    path('<int:id>/', EssayReviewDetailAPIView.as_view(), name = "essays-reviews-details"),
    #path('<int:id>/edit', EssayReviewDetailAPIView.as_view(), name = "essay reviews-edit"),#delete
]
