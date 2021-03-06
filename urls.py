from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/(?P<pk>\d+)/remove/$', views.todo_remove, name='todo_remove'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^todo/impressum/$', views.todo_impressum, name='todo_impressum'),
]
