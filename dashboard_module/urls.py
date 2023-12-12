from django.urls import path

from . import views

app_name = 'dashboard_module'

urlpatterns = [
  path('', views.index, name = 'index'),
]