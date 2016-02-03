from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='course-index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='course-detail'),
    url(r'^(?P<pk>[\w-]+)/edit_course/$', views.CourseUpdate.as_view(), name='course-edit'),
    url(r'^(?P<pk>[0-9]+)/delete_course/$', views.CourseDelete.as_view(), name='course-delete'),
    url(r'^(?P<course_id>[0-9]+)/subjects/(?P<subject_id>[0-9]+)/$', views.subject, name='subject-detail')
]
