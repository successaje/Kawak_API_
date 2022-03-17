from django.urls import path, include

from .views import WaitingListView

urlpatterns = [
    path('', WaitingListView.as_view(), name = 'waiting-list'),
]