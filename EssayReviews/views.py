from django.shortcuts import render
from django.db.models import Q

from rest_framework.generics import (
    #ListCreateAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListAPIView
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework import permissions

from EssayReviews.permissions import Isuser

from .serializers import (
    EssayReviewListSerializer,
    EssayReviewDetailSerializer,
    create_essaysreviews_serializer,
)

from .models import EssayReview

from Essay.permission import Isuser
from Essay.pagination import EssayLimitOffsetPagination, EssayPageNumberPagination

class EssayReviewListAPIView(ListAPIView):
    serializer_class = EssayReviewListSerializer
    #queryset = EssayReview.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['EssayReview', 'user__first_name']
    pagination_class =  EssayLimitOffsetPagination
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_queryset(self, *args, **kwargs):
        queryset_list = EssayReview.objects.filter(id__gte=0)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name_icontains=query) |
                Q(user__last_name_icontains=query)
            ).distinct()
        return queryset_list

        #return self.queryset.filter(user=self.request.user)
    

class EssayReviewCreateAPIView(CreateAPIView):
    #serializer_class = EssayReviewCreateSerializer
    queryset = EssayReview.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        model_type = self.request.GET.get('type')
        slug = self.request.GET.get('slug')
        parent_id = self.request.GET.get('parent_id', None)
        return create_essaysreviews_serializer(
            model_type=model_type,
            slug =slug, 
            parent_id=parent_id,
            user = self.request.user
            )         
        #super().get_serializer_class()

class EssayReviewDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = EssayReview.objects.filter(id__gte=0)
    serializer_class = EssayReviewDetailSerializer
    permission_classes = (permissions.IsAuthenticated, Isuser)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


