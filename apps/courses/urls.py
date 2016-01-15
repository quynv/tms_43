from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='course-index'),
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='course-detail'),
    url(r'^(?P<course_id>[0-9]+)/subjects/(?P<subject_id>[0-9]+)/$', views.subject, name='subject-detail')
]
