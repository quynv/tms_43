from django.conf.urls import url
from django.contrib.auth.decorators import permission_required
from . import views

loginUrl = '/admin/login'

urlpatterns = [
    url(r'^$', permission_required('is_superuser', login_url=loginUrl)(views.ListCourseView.as_view()), name='index'),
    url(r'^courses/$', permission_required('is_superuser', login_url=loginUrl)(views.ListCourseView.as_view()), name='listcourse'),
    url(r'^subjects/$', permission_required('is_superuser', login_url=loginUrl)(views.ListSubjectView.as_view()), name='listsubject'),
    url(r'^users/$', permission_required('is_superuser', login_url=loginUrl)(views.ListUserView.as_view()), name='listuser'),

    url(r'^courses/new/$', permission_required('is_superuser', login_url=loginUrl)(views.CreateCourseView.as_view()), name='createcourse'),
    url(r'^courses/change_status/$', permission_required('is_superuser', login_url=loginUrl)(views.UpdateStatusCourse.as_view()), name='changecourse'),
    url(r'^courses/(?P<pk>[0-9]+)/update/$', permission_required('is_superuser', login_url=loginUrl)(views.UpdateCourseView.as_view()), name='updatecourse'),
    url(r'^courses/(?P<pk>[0-9]+)/add-user/$', permission_required('is_superuser', login_url=loginUrl)(views.AddUser2Course.as_view()), name='addusertocourse'),
    url(r'^courses/delete/$', permission_required('is_superuser', login_url=loginUrl)(views.DeleteCourseView.as_view()), name='deletecourse'),

    url(r'^subjects/new/$', permission_required('is_superuser', login_url=loginUrl)(views.CreateSubjectView.as_view()), name='createsubject'),
    url(r'^subjects/change_status/$', permission_required('is_superuser', login_url=loginUrl)(views.UpdateStatusSubject.as_view()), name='changesubject'),
    url(r'^subjects/(?P<pk>[0-9]+)/update/$', permission_required('is_superuser', login_url=loginUrl)(views.UpdateSubjectView.as_view()), name='updatesubject'),
    url(r'^subjects/delete/$', permission_required('is_superuser', login_url=loginUrl)(views.DeleteSubjectView.as_view()), name='deletesubject'),

    url(r'^users/new/$', permission_required('is_superuser', login_url=loginUrl)(views.CreateUserView.as_view()), name='createuser'),
    url(r'^users/(?P<pk>[0-9]+)/update/$', permission_required('is_superuser', login_url=loginUrl)(views.UpdateUserView.as_view()), name='updateuser'),
    url(r'^users/delete/$', permission_required('is_superuser', login_url=loginUrl)(views.DeleteUserView.as_view()), name='deleteuser'),

    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                        {'next_page': '/admin/login/'}, name='logout'),
]

