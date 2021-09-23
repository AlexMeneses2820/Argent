from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView


class LoginFormView(LoginView):
    template_name = 'login/login.html'

  #  def dispatch(self, request, *args, **kwargs):
   #     if request.user.is_authenticated:
    #        return redirect('inicio')
     #   return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicia tu sección con nosotros'
        return context

