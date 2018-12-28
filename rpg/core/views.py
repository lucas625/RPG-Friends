from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Monstro
class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["monstros"] = Monstro.objects.all().order_by('level')
        return context