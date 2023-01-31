from django.contrib import admin

# Register your models here.
from schedule.models import Timetable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    pass
