from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404

class HomeView(TemplateView):
    template_name="home.html"
    