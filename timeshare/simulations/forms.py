from django import forms
from .models import SimulationRun

class CreateSimulationForm(forms.ModelForm):
    source = forms.FileField()

    class Meta:
        model = SimulationRun
        fields = [
            "source"
        ]
