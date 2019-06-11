from django.contrib import admin
from step_tracker.models import Steps

@admin.register(Steps)
class StepsAdmin(admin.ModelAdmin):
    pass
