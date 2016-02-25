from django.views import generic
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.core.urlresolvers import reverse
import json

from .models import Course, UserCourse
from .forms import CourseForm
from apps.subjects.forms import SubjectForm
from apps.tasks.forms import TaskForm
from apps.subjects.models import Subject, UserSubject
from apps.tasks.models import Task, UserTask
from django.contrib.auth.models import User


class IndexView(generic.ListView):
    template_name = 'courses/list_courses.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = CourseForm
        context['user_current'] = User.objects.get(id = self.request.user.id)
        context['usercourses'] = UserCourse.objects.filter(user_id = self.request.user)
        context['usercourse'] = [usercourse.course_id for usercourse in context['usercourses']]
        return context

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                json.dumps({
                    'success': 1
                }),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({
                    'success': 0,
                    'errors': dict(form.errors.items()),
                }),
                content_type="application/json"
            )


class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = SubjectForm
        context['user_current'] = User.objects.get(id = self.request.user.id)
        context['subjects'] = Subject.objects.filter(course=self.object)
        context['usercourses'] = UserCourse.objects.filter(user_id = self.request.user)
        context['usercourse'] = [usercourse.course_id for usercourse in context['usercourses']]
        context['usersubjects'] = UserSubject.objects.filter(user_id = self.request.user)
        context['usersubject'] = [usersubject.subject_id for usersubject in context['usersubjects']]
        return context

    def post(self, request, pk):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                json.dumps({
                    'success': 1
                }),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({
                    'success': 0,
                    'errors': dict(form.errors.items()),
                }),
                content_type="application/json"
            )


class CourseUpdate(generic.UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_edit.html'
    success_url = '/courses/'


class CourseDelete(generic.DeleteView):
    def get(self, request, pk):
        Course.objects.get(pk=pk).delete()
        return HttpResponseRedirect("/courses/")


class UserCourseJoin(generic.UpdateView):
    def get(self, request, pk, **kwargs):
        user = User.objects.get(pk = request.user.id)
        course = Course.objects.get(pk = pk)
        if UserCourse.objects.filter(course = course, user = user):
            return HttpResponseRedirect("/courses/")
        else:
            usercourse = UserCourse(course = course, user = user)
            usercourse.save()
            return HttpResponseRedirect("/courses/")


class SubjectDetail(generic.DetailView):
    model = Subject
    template_name = 'subjects/subject_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectDetail, self).get_context_data(**kwargs)
        context['form'] = TaskForm
        context['user_current'] = User.objects.get(id = self.request.user.id)
        context['tasks'] = Task.objects.filter(subject=self.object)
        context['usercourses'] = UserCourse.objects.filter(user_id = self.request.user)
        context['usercourse'] = [usercourse.course_id for usercourse in context['usercourses']]
        context['usertasks'] = UserTask.objects.filter(user_id = self.request.user)
        context['usertask'] = [usertask.task_id for usertask in context['usertasks']]
        context['course_id'] = int(self.kwargs['course_id'])
        return context

    def post(self, request, pk, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            object = Task(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
            )
            object.save()
            object.subject.add(Subject.objects.get(pk=pk))
            return HttpResponse(
                json.dumps({
                    'success': 1
                }),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({
                    'success': 0,
                    'errors': dict(form.errors.items()),
                }),
                content_type="application/json"
            )


class SubjectUpdate(generic.UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/subject_edit.html'
    def get_success_url(self, **kwargs):
        course_id = self.kwargs['course_id']
        return reverse('courses:course-detail', kwargs={'pk' : course_id})


class SubjectDelete(generic.DeleteView):
    def get(self, request, pk, **kwargs):
        Subject.objects.get(pk=pk).delete()
        course_id = self.kwargs['course_id']
        url = reverse('courses:course-detail', kwargs={'pk': course_id})
        return HttpResponseRedirect(url)


class UserSubjectChangeStatus(generic.UpdateView):
    def get(self, request, pk, **kwargs):
        user = User.objects.get(pk = request.user.id)
        subject = Subject.objects.get(pk = pk)
        if UserSubject.objects.filter(subject = subject, user = user):
            usersubject = UserSubject.objects.get(subject = subject, user = user)
            if usersubject:
                if usersubject.status == 'finish':
                    usersubject.status = 'doing'
                else:
                    usersubject.status = 'finish'
        else:
            usersubject = UserSubject(subject = subject, user = user, status = "finish")
        usersubject.save()
        course_id = self.kwargs['course_id']
        url = reverse('courses:course-detail', kwargs={'pk': course_id})
        return HttpResponseRedirect(url)


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    def get_success_url(self, **kwargs):
        course_id = self.kwargs['course_id']
        subject_id = self.kwargs['subject_id']
        return reverse('courses:subject-detail', kwargs={'course_id' : course_id, 'pk' : subject_id})


class TaskDelete(generic.DeleteView):
    def get(self, request, pk, **kwargs):
        Task.objects.get(pk=pk).delete()
        course_id = self.kwargs['course_id']
        subject_id = self.kwargs['subject_id']
        url = reverse('courses:subject-detail', kwargs={'course_id' : course_id, 'pk' : subject_id})
        return HttpResponseRedirect(url)


class UserTaskChangeStatus(generic.UpdateView):
    def get(self, request, pk, **kwargs):
        user = User.objects.get(pk = request.user.id)
        task = Task.objects.get(pk = pk)
        if UserTask.objects.filter(task = task, user = user):
            usertask = UserTask.objects.get(task = task, user = user)
            if usertask:
                if usertask.status == 'finish':
                    usertask.status = 'doing'
                else:
                    usertask.status = 'finish'
        else:
            usertask = UserTask(task = task, user = user, status = "finish")
        usertask.save()
        course_id = self.kwargs['course_id']
        subject_id = self.kwargs['subject_id']
        url = reverse('courses:subject-detail', kwargs={'course_id' : course_id, 'pk' : subject_id})
        return HttpResponseRedirect(url)
