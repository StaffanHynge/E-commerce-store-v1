from django.contrib import admin
from .models import Events


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "location",
        "date",
        "time",
        "image"
    )
