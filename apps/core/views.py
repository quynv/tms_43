__author__ = 'javimuu'

from django.views.generic.detail import ContextMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.views.decorators.gzip import gzip_page

# from apps.categories.models import Category
# from apps.books.models import Book, UserProfileBook
# from apps.reviews.models import Review

# from apps.carts import utils

class BaseView(ContextMixin):
    """docstring for BaseView"""
    @method_decorator(gzip_page)
    def dispatch(self, request, *args, **kwargs):
        return super(BaseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        info = {
            # 'list_lastest_post': Blog.objects.order_by('-id')[:5],
            # 'list_lastest_subject': Subject.objects.all()[:3],
            # 'list_popular_subject': Subject.objects.order_by('?')[:3],
            # 'list_category': Category.objects.all(),
            # 'list_latest_comment': Comment.objects.order_by('-id')[:3]
        }
        context.update(info)
        return context


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
