from django.views.generic.base import TemplateView
from django.shortcuts import render

class PageIndexView(TemplateView):
    template_name = "Core/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Mi Super Web Playground"})

class PageSampleView(TemplateView):
    template_name = "Core/sample.html"