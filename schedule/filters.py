from django_filters import rest_framework

from schedule.models import Timetable


class TimetableFilter(rest_framework.FilterSet):
    class Meta:
        model = Timetable
        fields = ['group__name', 'room__number', 'teacher__name']
