from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views import generic
from apps.reports.models import Report
from apps.reports.forms import ReportForm
import json
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'reports/index.html'
    model = Report
    context_object_name = 'reports'
    paginate_by = 6
    queryset = Report.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = ReportForm
        return context

    def post(self, request):
        form = ReportForm(request.POST)
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


class DetailView(generic.View):
    def get(self, request, id):
        params = dict()
        params['report'] = Report.objects.get(pk=id)
        return render(request, 'reports/view.html', params)


class EditView(generic.View):
    def get(self, request, id):
        report = get_object_or_404(Report, pk=id)
        params = dict()
        params['report'] = report
        params['form'] = ReportForm(instance=report)
        return render(request, 'reports/edit.html', params)

    def post(self, request, id):
        report = get_object_or_404(Report, pk=id)
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reports:detail', args=(report.id, )))
        else:
            params = dict()
            params['report'] = report
            params['form'] = form
            return render(request, 'reports/edit.html', params)


class DeleteView(generic.View):
    def post(self, *args, **kwargs):
            id = self.request.POST.get('id')
            # report = Report.objects.filter(id=id, user_id=request.user.id);
            report = Report.objects.get(pk=id)
            if report:
                report.delete()
                return HttpResponse(
                    json.dumps({
                        'success': 1,
                        'message': 'Report has been removed'
                    }),
                    content_type="application/json"
                )
            else:
                return HttpResponse(
                    json.dumps({
                        'success': 0,
                        'message': 'Can\' delete this post'
                    }),
                    content_type="application/json"
                )