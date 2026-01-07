from django.contrib import admin

from routine.models import Routine


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ("class_name", "subject", "teacher", "day", "start_time", "end_time", "room")
    search_fields = ("class_name", "subject", "teacher")
    list_filter = ("day", "class_name")
