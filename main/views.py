from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, generics, views

from .serializers import WaitingList

class WaitingListView(generics.GenericAPIView):

    serializer_class = WaitingList

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status = status.HTTP_201_CREATED)
