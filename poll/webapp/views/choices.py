from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choices/choice_create_view.html'
    form_class = ChoiceForm

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        kwargs['poll'] = poll
        return kwargs

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return super().form_valid(form)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choices/choice_update_view.html'
    form_class = ChoiceForm

