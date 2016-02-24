from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='course-index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='course-detail'),
    url(r'^(?P<pk>[\w-]+)/edit-course/$', views.CourseUpdate.as_view(), name='course-edit'),
    url(r'^(?P<pk>[0-9]+)/delete-course/$', views.CourseDelete.as_view(), name='course-delete'),
    url(r'^(?P<course_id>[0-9]+)/subjects/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view(), name='subject-detail'),
    url(r'^(?P<course_id>[0-9]+)/subjects/(?P<pk>[0-9]+)/edit-subject/$', views.SubjectUpdate.as_view(), name='subject-edit'),
    url(r'^(?P<course_id>[0-9]+)/subjects/(?P<pk>[0-9]+)/delete-subject/$', views.SubjectDelete.as_view(), name='subject-delete'),
    url(r'^(?P<course_id>[0-9]+)/subjects/(?P<subject_id>[0-9]+)/tasks/(?P<pk>[0-9]+)/edit-task/$',
        views.TaskUpdate.as_view(), name='task-edit'),
    url(r'^(?P<course_id>[0-9]+)/subjects/(?P<subject_id>[0-9]+)/tasks/(?P<pk>[0-9]+)/delete-task/$',
        views.TaskDelete.as_view(), name='task-delete'),
    url(r'^(?P<course_id>[0-9]+)/subjects/(?P<subject_id>[0-9]+)/tasks/(?P<pk>[0-9]+)/usertask-change-status/$',
        views.UserTaskChangeStatus.as_view(), name='usertask-change-status')
]
