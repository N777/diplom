from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import mixins, viewsets

from schedule.models import Timetable
from schedule.serializers import TimetableSerializer


class TimetableViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    """Расписание."""

    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = (DjangoFilterBackend,)
