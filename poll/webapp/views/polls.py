from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from webapp.models import Poll


class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list_view.html'
    context_object_name = 'polls'
