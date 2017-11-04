from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import EditorForm
from .models import RealEditor


class EditorMSG(generic.CreateView):
    model = RealEditor
    template_name = 'home.html'
    success_url = '#'
    form_class = EditorForm

    def get_context_data(self, *args, **kwargs):
        context = super(EditorMSG, self).get_context_data(*args, **kwargs)
        context['editors'] = RealEditor.objects.order_by('-pk')[:10]
        return context

    def form_valid(self, form):
        response = super(EditorMSG, self).form_valid(form)
        rt_msg = self.object
        rt_msg.editor_text = rt_msg.message
        rt_msg.save()
        return response
