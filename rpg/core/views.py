from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Monstro, Mapa, Habilidade, Classe, Raca, Item
class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["monstros"] = Monstro.objects.all()
        context["mapas"] = Mapa.objects.all()
        context["habilidades"] = Habilidade.objects.all()
        context["classes"] = Classe.objects.all()
        context["racas"] = Raca.objects.all()
        context["itens"] = Item.objects.all()
        return context