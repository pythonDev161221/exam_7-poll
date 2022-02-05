from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from webapp.models import Answer, Poll, Choice


class AnswerView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        poll = get_object_or_404(Poll, pk=(self.kwargs.get('pk')))
        context['poll'] = poll
        context['choices'] = poll.choices.all()
        diction = {}
        c = 0
        for ch in poll.choices.all():
            for ans in poll.answers.all():
                if ans.choice == ch:
                    c += 1
                    diction[ch] = c
        list_dict = []
        for i, j in diction.items():
            list_dict.append([i, j])
        # context['list_dict'] = list_dict
        # summ = 0
        # for i in list_dict:
        #     summ = summ + i[1]
        # for i in range(len(list_dict)):
        #     list_dict[i][2] = list_dict[i]*100/summ
        context['list_dict'] = list_dict
        return render(request, 'answers/answer_view.html', context)

    def post(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=(self.kwargs.get('pk')))
        choice_pk = request.POST.get('choice')
        choice = get_object_or_404(Choice, pk=choice_pk)
        answer = Answer()
        answer.poll = poll
        answer.choice = choice
        answer.save()
        return redirect("poll_list_view")



# class AnswerView(CreateView):
#     template_name = 'answers/answer_view.html'
#     model = Answer
#
#     def get_context_data(self, **kwargs):
#         kwargs = super().get_context_data(**kwargs)
#         poll = get_object_or_404(Poll, pk=(self.kwargs.get('pk')))
#         kwargs['poll'] = poll
#         kwargs['choices'] = poll.choices.all()
#         return kwargs
#
#     # def get(self, request, *args, **kwargs):
#     #     context = {}
#     #     poll = get_object_or_404(Poll, pk=(self.kwargs.get('pk')))
#     #     context['poll'] = poll
#     #     context['choices'] = poll.choices.all()
#     #     return render(request, 'answers/answer_view.html', context)
#
#     def post(self, request, *args, **kwargs):
#         print('post start')
#         poll = get_object_or_404(Poll, pk=(self.kwargs.get('pk')))
#         choice_pk = request.POST.get('choice')
#         choice = get_object_or_404(Choice, pk=choice_pk)
#         answer = Answer()
#         answer.poll = poll
#         answer.choice = choice
#         answer.save()
#         print('post finish')
#         return super(AnswerView, self).post(request, *args, **kwargs)

    # template_name = 'polls/poll_list_view.html'
    # model = Poll