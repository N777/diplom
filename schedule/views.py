from datetime import timedelta

from django.db.models import Q
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from schedule.filters import TimetableFilter
from schedule.models import *
from schedule.serializers import *
from schedule.services import TimetablePrintService, TimetableParseService


class TimetableViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """Расписание."""

    serializer_class = TimetableSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TimetableFilter
    search_fields = ['group__name', 'room__number', 'teacher__name']

    def get_queryset(self):
        today = datetime.datetime.today()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_second_week = start_of_week + timedelta(days=14)
        regular_filter = Q(once=False)
        current_events_filter = Q(date__gte=start_of_week) & Q(date__lte=end_of_second_week) & Q(once=True)
        union_qs = Timetable.objects.filter(regular_filter | current_events_filter)
        return union_qs

    def perform_destroy(self, instance):
        if instance.date:
            qs_to_delete = Timetable.objects.filter(date=instance.date, start_time=instance.start_time,
                                                    end_time=instance.end_time)
            qs_to_delete.delete()
        else:
            instance.delete()


# http://127.0.0.1:8000/api/print-timetable/?groups=%D0%98%D0%92%D0%A2%D0%90%D0%9F%D0%B1%D0%B4-21
class TimetablePrintView(APIView):
    service = TimetablePrintService
    queryset = Timetable.objects.filter(once=False)

    def get(self, request):
        names = request.GET.get('names')
        if not names:
            return Response(status=HTTP_400_BAD_REQUEST)
        names = [group.strip() for group in names.split(',')]
        schedule_content = ''

        for find in names:
            qs = self.queryset.filter(
                Q(group__name__contains=find) | Q(room__number__contains=find) | Q(teacher__name__contains=find))
            schedule_content += self.service().get_timetable_html(qs, find)

        response = HttpResponse(schedule_content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="schedule.html"'
        return response


class TimetableResetView(APIView):
    service = TimetableParseService

    def post(self, request):
        self.service().reset_timetable()
        return Response()


class EventTimetableViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Timetable.objects.all()
    serializer_class = EventTimetableSerializer


class LessonTimetableViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
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
