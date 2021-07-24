from django.contrib import admin
from django_dbq.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
