from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import PollForm
from webapp.models import Poll


class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list_view.html'
    context_object_name = 'polls'
    paginate_by = 5
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        return queryset


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls/poll_detail_view.html'


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/poll_create_view.html'
