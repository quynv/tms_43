from django.views import generic

from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Course
from apps.subjects.models import Subject


class IndexView(generic.ListView):
    template_name = 'courses/list_courses.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-created_at')[:5]


def detail(request, course_id):
    context = RequestContext(request)
    course_id = course_id
    context_dict = {'course_id': course_id}
    try:
        course = Course.objects.get(id=course_id)
        subjects = Subject.objects.filter(course=course)
        context_dict['subjects'] = subjects
        context_dict['course'] = course
    except Course.DoesNotExist:
        pass
    return render_to_response('courses/course_detail.html', context_dict, context)


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