from django.urls import path
from core.login.views.login.views import *
urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('Logout/', LogoutRedirectView.as_view(), name='Logout'),
]