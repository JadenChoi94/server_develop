# todo/urls.py
from django.conf.urls import url
from . import views


urlpatterns = [
    url('create', views.TaskCreate.as_view(), name='create'),
    url('select', views.TaskSelect.as_view(), name='select'),
    url('', views.Todo.as_view(), name='todo'),
]