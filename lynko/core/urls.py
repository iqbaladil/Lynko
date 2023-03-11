from django.contrib import admin
from django.urls import path
from core.views import index

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
