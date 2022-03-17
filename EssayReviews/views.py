from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .serializers import EssayReviewSerializer
from .models import EssayReview
from .permissions import IsReviewer

class EssayReviewListAPIView(ListCreateAPIView):

    serializer_class = EssayReviewSerializer
    queryset = EssayReview.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(Reviewer=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Reviewer=self.request.user)

class EssayReviewDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = EssayReviewSerializer
    queryset = EssayReview.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsReviewer)
    lookup_fields = "id"

    # def perform_create(self, serializer):
    #     return serializer.save(Reviewer=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Reviewer=self.request.user)


