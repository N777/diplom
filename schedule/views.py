from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from schedule.filters import TimetableFilter
from schedule.models import *
from schedule.serializers import *


class TimetableViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                       viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """Расписание."""

    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TimetableFilter
    search_fields = ['group__name', 'room__number', 'teacher__name']


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
