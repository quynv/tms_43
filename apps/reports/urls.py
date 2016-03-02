from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/user/$', views.IndexView.as_view(), name='reports'),
    url(r'^(?P<id>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<id>[0-9]+)/edit/$', views.EditView.as_view(), name='edit'),
    url(r'^delete/$', views.DeleteView.as_view(), name='delete'),
]
