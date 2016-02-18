from django.views import generic
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
import json
from django.core.urlresolvers import reverse_lazy
from django.http import Http404

from .models import Course
from .forms import CourseForm
from .forms import SubjectForm, TaskForm
from apps.subjects.models import Subject
from apps.tasks.models import Task


class IndexView(generic.ListView):
    template_name = 'courses/list_courses.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = CourseForm
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
        context['subjects'] = Subject.objects.filter(course=self.object)
        return context

    def post(self, request, pk):
        form = SubjectForm(request.POST)
        if form.is_valid():
            object = Subject(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
            )
            object.save()
            object.course.add(Course.objects.get(pk=pk))
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


class SubjectDetail(generic.DetailView):
    model = Subject
    template_name = 'subjects/subject_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectDetail, self).get_context_data(**kwargs)
        context['form'] = TaskForm
        context['tasks'] = Task.objects.filter(subject=self.object)
        context['course_id'] = self.kwargs['course_id']
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


class TaskChangeStatus(generic.UpdateView):
    def get(self, request, pk, **kwargs):
        # Task.objects.get(pk=pk).delete()
        task = Task.objects.get(pk=pk)
        if task.status == 'finish':
            task.status = 'doing'
        else:
            task.status = 'finish'
        task.save()
        course_id = self.kwargs['course_id']
        subject_id = self.kwargs['subject_id']
        url = reverse('courses:subject-detail', kwargs={'course_id' : course_id, 'pk' : subject_id})
        return HttpResponseRedirect(url)
