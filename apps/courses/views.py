from django.views import generic
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
import json

from .models import Course
from .forms import CourseForm
from .forms import SubjectForm
from apps.subjects.models import Subject


class IndexView(generic.ListView):
    template_name = 'courses/list_courses.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-created_at')[:5]

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


def subject(request, course_id, subject_id):
    context = RequestContext(request)
    subject_id = subject_id
    context_dict = {'subject_id': subject_id}
    try:
        subject = Subject.objects.get(id=subject_id)
        context_dict['subject'] = subject
    except Subject.DoesNotExist:
        pass
    return render_to_response('subjects/subject_detail.html', context_dict, context)
