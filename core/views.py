from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class SomeView(View):
    def get(self, request):
        return render(request, 'some.html')

    def post(self, request):
        request.POST
        pass
