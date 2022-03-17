from django.shortcuts import render
from .serializers import Contact_Us_Serializer

from rest_framework import generics, status 
from rest_framework.response import Response

# Create your views here.
class Contact_UsAPIView(generics.GenericAPIView):

    serializer_class = Contact_Us_Serializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception= True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status = status.HTTP_201_CREATED)