from django.shortcuts import HttpResponse
from django.views import generic
from apps.activities.models import Activity
import json
# Create your views here.


class IndexView(generic.ListView):
    template_name = "activities/index.html"
    model = Activity
    context_object_name = 'activities'
    paginate_by = 20
    queryset = Activity.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

    def post(self, request):
        id = request.POST.get('id')
        # activity = Activity.objects.filter(id=id, user_id=request.user.id);
        activity = Activity.objects.get(pk=id)
        if activity:
            activity.delete()
            return HttpResponse(
                json.dumps({
                    'success': 1,
                    'message': 'Activity has been removed'
                }),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({
                    'success': 0,
                    'message': 'Can\' delete this activity log'
                }),
                content_type="application/json"
            )
