from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import login, logout
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages

from apps.courses.models import Course
from apps.subjects.models import Subject
from apps.courses.forms import CourseForm
from apps.subjects.forms import SubjectForm
from apps.users.models import UserProfile
from .forms import UserForm
import json
# Create your views here.


class LoginView(generic.FormView):
    form_class = AdminAuthenticationForm
    template_name = 'admin/login.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.is_staff:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:listcourse')

    def form_valid(self, form):
        admin = form.get_user()
        login(self.request, admin)
        return super().form_valid(form)


class ListCourseView(generic.ListView):
    template_name = 'admin/index.html'
    model = Course
    context_object_name = 'courses'
    paginate_by = 20
    queryset = Course.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(ListCourseView, self).get_context_data(**kwargs)
        return context


class ListSubjectView(generic.ListView):
    template_name = 'admin/subjects/index.html'
    model = Subject
    context_object_name = 'subjects'
    paginate_by = 20
    queryset = Subject.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(ListSubjectView, self).get_context_data(**kwargs)
        return context


# class ListTaskView(ListView):
#     template_name = 'admin/index.html'
#     model = Task
#     context_object_name = 'tasks'
#     paginate_by = 20
#     queryset = Course.objects.order_by('-created_at')
#
#     def get_context_data(self, **kwargs):
#         context = super(ListTaskView, self).get_context_data(**kwargs)
#         return context

class CreateCourseView(generic.CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'admin/courses/course_new.html'
    success_url = '/admin/'


class UpdateCourseView(generic.UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'admin/courses/course_edit.html'
    success_url = '/admin/'


class DeleteCourseView(generic.View):
    def post(self, *args, **kwargs):
            id = self.request.POST.get('id')
            course = Course.objects.get(pk=id)
            if course:
                course.delete()
                return HttpResponse(
                    json.dumps({
                        'success': 1,
                        'message': 'Course has been removed'
                    }),
                    content_type="application/json"
                )
            else:
                return HttpResponse(
                    json.dumps({
                        'success': 0,
                        'message': 'Course not found with id: '+id
                    }),
                    content_type="application/json"
                )


class CreateSubjectView(generic.CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'admin/subjects/subject_new.html'
    success_url = '/admin/subjects'


class UpdateSubjectView(generic.UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'admin/subjects/subject_edit.html'
    success_url = '/admin/subjects'


class DeleteSubjectView(generic.View):
    def post(self, *args, **kwargs):
            id = self.request.POST.get('id')
            subject = Subject.objects.get(pk=id)
            if subject:
                subject.delete()
                return HttpResponse(
                    json.dumps({
                        'success': 1,
                        'message': 'Subject has been removed'
                    }),
                    content_type="application/json"
                )
            else:
                return HttpResponse(
                    json.dumps({
                        'success': 0,
                        'message': 'Subject not found with id: '+id
                    }),
                    content_type="application/json"
                )


class CreateUserView(generic.CreateView):
    model = User
    form_class = UserForm
    template_name = 'admin/users/new.html'
    success_url = '/admin/users'

    def form_valid(self, form, **kwargs):
        self.object = form.save()
        profile = UserProfile.objects.create(user=self.object)
        profile.save()

        messages.success(self.request, "You signed up successfully,\
                                    You can log in now.")

        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data(**kwargs)
        return context


class UpdateUserView(generic.UpdateView):
    model = User
    form_class = UserForm
    template_name = 'admin/users/edit.html'
    success_url = '/admin/users'


class ListUserView(generic.ListView):
    template_name = 'admin/users/index.html'
    model = User
    context_object_name = 'users'
    paginate_by = 20

    def get_queryset(self):
        type = self.request.GET.get('type')
        is_superuser = 1
        if type == 'trainee':
            is_superuser = 0
        return User.objects.filter(is_superuser=is_superuser).order_by('-date_joined')

    def get_context_data(self, **kwargs):
        context = super(ListUserView, self).get_context_data(**kwargs)
        type = self.request.GET.get('type')
        if not type:
            type = 'supervisor'
        context['type'] = type
        return context


class DeleteUserView(generic.View):
    def post(self, *args, **kwargs):
            id = self.request.POST.get('id')
            user = User.objects.get(pk=id)
            if user:
                user.delete()
                return HttpResponse(
                    json.dumps({
                        'success': 1,
                        'message': 'User has been removed'
                    }),
                    content_type="application/json"
                )
            else:
                return HttpResponse(
                    json.dumps({
                        'success': 0,
                        'message': 'User not found with id: '+id
                    }),
                    content_type="application/json"
                )