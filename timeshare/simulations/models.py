from django.db import models


class SimulationRun(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    source = models.FileField(null=True)

    class Meta:
        ordering = ["-created"]
