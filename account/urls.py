from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login')
]
