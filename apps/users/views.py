from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.conf import settings
from django.apps import apps as django_apps
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
        UserCreationForm,
        AuthenticationForm,
)
from django.views.generic import View
from django.template import RequestContext

from apps.core.views import BaseView, LoginRequiredMixin
from apps.users.models import UserProfile, Document
from apps.users.forms import DocumentForm, UserCreateForm, UserEditForm

# Create your views here.
class SignupUserView(BaseView, CreateView):
    model = django_apps.get_model(settings.AUTH_USER_MODEL)
    form_class = UserCreateForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        profile = UserProfile.objects.create(user=self.object)
        profile.save()

        messages.success(self.request, "You signed up successfully,\
                                    You can log in now.")

        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Signup'
            },
            'page_title': 'Sign Up',
        }
        context.update(info)
        return context


class LoginUserView(BaseView, FormView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.success_url)
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Login'
            },
            'page_title': 'Login',
        }
        context.update(info)
        return context

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

class LogoutUserView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('users:login'))

class Index(View):
    def get(self, request):
        params  = dict()
        params["name"] = "javimuu"
        return render(request, 'subjects/index.html', params)


@login_required
def change_avatar(request):
    # Handle file upload
    user = get_object_or_404(User, pk = request.user.id)

    if request.method == 'POST':
        form = UserEditForm(instance=user)
        ava_form = DocumentForm(request.POST, request.FILES)
        if ava_form.is_valid():
            profile = UserProfile(user = request.user, avatar= request.FILES['avatar'])
            profile.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('users:avatar'))
    else:
        form = UserEditForm(instance=user)
        ava_form = DocumentForm


    # Render list page with the documents and the form
    return render_to_response('users/setting.html', {'user': user, 'form': form , 'ava_form': ava_form}, context_instance = RequestContext(request))


@login_required
def edit_profile(request):
    # Handle file upload
    user = get_object_or_404(User, pk = request.user.id)
    profile_form = UserEditForm(instance=user)
    if request.method == 'POST':
        user = get_object_or_404(User, pk = request.user.id)
        profile_form = UserEditForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('users:setting'))

    # Render list page with the documents and the form
    return render_to_response('users/setting.html', {'user': user, 'form': profile_form}, context_instance = RequestContext(request))
