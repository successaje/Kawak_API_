from django.shortcuts import render

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

from rest_framework import permissions

from .serializers import (
    EssayListSerializer,
    EssayDetailSerializer,
    EssayCreateSerializer,
)

from .models import Essay
from .permission import Isuser
from .pagination import EssayLimitOffsetPagination, EssayPageNumberPagination

class EssayListAPIView(ListAPIView):
    serializer_class = EssayListSerializer
    queryset = Essay.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'user', 'Topic']
    pagination_class =  EssayLimitOffsetPagination
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    

class EssayCreateAPIView(CreateAPIView):
    serializer_class = EssayCreateSerializer
    queryset = Essay.objects.all()
    lookup_field = 'id'

    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class EssayDeleteAPIView(DestroyAPIView):
    serializer_class = EssayDetailSerializer
    queryset = Essay.objects.all()
    lookup_field = 'id' 

    permission_classes = (permissions.IsAuthenticated,)


class EssayDetailAPIView(RetrieveAPIView):
    serializer_class = EssayDetailSerializer
    queryset = Essay.objects.all()
    permission_classes = (permissions.IsAuthenticated, Isuser)
    lookup_fields = "id"

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


