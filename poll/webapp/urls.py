from django.contrib import admin
from django.urls import path

from webapp.views import PollListView

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list_view'),
]