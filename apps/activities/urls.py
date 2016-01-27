from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='activities'),
    url(r'^delete/$', views.DeleteView.as_view(), name='delete'),
]
