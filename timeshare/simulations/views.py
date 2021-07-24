from django.views.generic import TemplateView, CreateView, DetailView
from .models import SimulationRun
from . import forms
from django.http import HttpResponseRedirect
from django_dbq.models import Job

class IndexView(TemplateView):
    template_name = 'index.html'


class CreateSimulationView(CreateView):
    model = SimulationRun
    form_class = forms.CreateSimulationForm
    template_name = "create_simulation.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        Job.objects.create(name="run_simulation", workspace={"simulation_id": obj.id})
        return HttpResponseRedirect("/")


class SimulationDetailView(DetailView):
    template_name = "simulation.html"

    def get_queryset(self):
        return SimulationRun.objects.filter(user=self.request.user)
