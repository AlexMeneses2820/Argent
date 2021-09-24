from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from app.settings import LOGIN_REDIRECT_URL


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView


class LoginFormView(LoginView):
    template_name = 'login/login.html'
    success_url = reverse_lazy(LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(LOGIN_REDIRECT_URL)
            return redirect('inicio')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicia tu sección con nosotros'
        return context

class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
