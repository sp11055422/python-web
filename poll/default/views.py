from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView
from .models import Poll, Option


# 列表視圖 (ListView)
class PollList(ListView):
    model = Poll
    template_name = 'default/poll_list.html'
    context_object_name = 'poll_list'


# 單一 Poll 詳細頁 (DetailView)
class PollView(DetailView):
    model = Poll
    template_name = 'default/list.html'
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['option_list'] = self.object.options.all()
        return ctx


# 投票動作 (增加票數後導回該 poll 的詳細頁)
class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        oid = self.kwargs.get('oid')
        option = get_object_or_404(Option, id=oid)
        option.votes = option.votes + 1
        option.save()
        return reverse('poll_view', args=[option.poll.id])


# 建立與編輯視圖
class PollCreate(CreateView):
    model = Poll
    fields = ['subject', 'desc']
    template_name = 'default/poll_form.html'
    success_url = reverse_lazy('poll_list')


class PollEdit(UpdateView):
    model = Poll
    fields = ['subject', 'desc']
    template_name = 'default/poll_form.html'
    success_url = reverse_lazy('poll_list')