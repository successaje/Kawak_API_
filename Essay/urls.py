from django.urls import path

from . import views

urlpatterns = [
    path('', views.EssayListAPIView.as_view(), name = "essays"),
    path('<int:id>', views.EssayDetailAPIView.as_view(), name = "essay"),
]
