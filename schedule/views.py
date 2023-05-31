from datetime import timedelta

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from schedule.filters import TimetableFilter
from schedule.models import *
from schedule.serializers import *


# TODO что делать с 2-СЗ

class TimetableViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                       viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """Расписание."""

    serializer_class = TimetableSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TimetableFilter
    search_fields = ['group__name', 'room__number', 'teacher__name']

    def get_queryset(self):
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_second_week = start_of_week + timedelta(days=14)
        regular_filter = Q(once=False)
        current_events_filter = Q(start_time__gte=start_of_week) & Q(end_time__lte=end_of_second_week) & Q(once=True)
        union_qs = Timetable.objects.filter(regular_filter | current_events_filter)
        return union_qs


class EventTimetableViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Timetable.objects.all()
    serializer_class = EventTimetableSerializer


class LessonTimetableViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Timetable.objects.all()
    serializer_class = LessonTimetableSerializer


class GroupViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer


class TeacherViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Teacher.objects.all().order_by('name')
    serializer_class = TeacherSerializer


class RoomViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Room.objects.all().order_by('number')
    serializer_class = RoomSerializer


class LessonViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Lesson.objects.all().order_by('name')
    serializer_class = LessonSerializer


class LessonsTimesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = LessonsTimes.objects.all().order_by('id')
    serializer_class = LessonsTimesSerializer
