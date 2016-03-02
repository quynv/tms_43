__author__ = 'javimuu'

from django.conf.urls import url
from apps.users import views


urlpatterns = [
        url(r'^signup/$', views.SignupUserView.as_view(), name='signup'),
        url(r'^login/$', views.LoginUserView.as_view(), name='login'),
        url(r'^logout/$', views.LogoutUserView.as_view(), name='logout'),
        url(r'^avatar/$',views.change_avatar, name='avatar'),
        url(r'^setting/$',views.edit_profile, name='setting'),
        url(r'^(?P<pk>[0-9]+)/profile/$', views.UserProfileView.as_view(), name='profile'),
]
