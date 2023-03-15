from django.urls import path
from . import views

app_name = 'links'

urlpatterns = [
    path('', views.links, name='links'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-link/', views.create_link, name='create_link'),
]
