from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name ='user'

urlpatterns = [
    path('register/', views.register_patsient_view, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'),name='login'),
]