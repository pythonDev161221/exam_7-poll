from django.contrib import admin
from django.urls import path

from webapp.views import PollListView, PollDetailView, PollCreateView, PollUpdateView, PollDeleteView

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list_view'),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_detail_view'),
    path('poll/create/', PollCreateView.as_view(), name='poll_create_view'),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name='poll_update_view'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete_view'),

]
