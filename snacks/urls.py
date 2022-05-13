import imp
from django.urls import path
from .views import SnackListView, SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='snacks_list'),
    path('detail-view/<int:pk>', SnackDetailView.as_view(), name='snacks_detail'),
]