from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(form_class=LoginForm), name='login'),
]
