from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from schedule.filters import TimetableFilter
from schedule.models import Timetable
from schedule.serializers import TimetableSerializer


class TimetableViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    """Расписание."""

    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TimetableFilter
    search_fields = ['group__name', 'room__number', 'teacher__name']
