from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from schedule.filters import TimetableFilter
from schedule.models import Timetable, Group
from schedule.serializers import TimetableSerializer, GroupSerializer


class TimetableViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """Расписание."""

    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TimetableFilter
    search_fields = ['group__name', 'room__number', 'teacher__name']


class GroupViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer