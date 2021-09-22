from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from core.Chat.models import Chat


class ChatListview(ListView):
    template_name = 'Chat/Chat.html'
    model = Chat
    sucess_url = reverse_lazy('Chat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Chat_url'] = reverse_lazy('Chat')
        return context

