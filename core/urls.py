from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from core.views import HomeView, SomeView

urlpatterns = [
    #path('', TemplateView.as_view(template_name='index.html')),
    path('', HomeView.as_view()),
    path('some/', SomeView.as_view()),
    #path('id<int:user_id>', HomeView.as_view()),
]