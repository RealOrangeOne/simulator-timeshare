from django.db import models
from django_dbq.models import Job


class SimulationRun(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    source = models.FileField(null=True)

    class Meta:
        ordering = ["-created"]

    @property
    def job(self):
        return Job.objects.filter(workspace__simulation_id=self.id).latest('created')
