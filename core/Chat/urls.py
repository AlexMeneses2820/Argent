from django.urls import path
from core.Chat.views.Chat.views import *

urlpatterns = [
    path('Chat/', ChatListview.as_view(), name='Chat'),
]