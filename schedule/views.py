from datetime import timedelta

from django.db.models import Q
from django.http import HttpResponse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

from schedule.filters import TimetableFilter
from schedule.models import *
from schedule.serializers import *
from schedule.services import TimetablePrintService


# TODO что делать с 2-СЗ

class TimetableViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin):
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


# http://127.0.0.1:8000/api/print-timetable/?groups=%D0%98%D0%92%D0%A2%D0%90%D0%9F%D0%B1%D0%B4-21
class TimetablePrintView(APIView):
    service = TimetablePrintService
    queryset = Timetable.objects.filter(once=False)

    def get(self, request):
        group_names = request.GET.get('groups', '')
        group_names = [group.strip() for group in group_names.split(',')]
        schedule_content = ''
        # Ваш код для генерации расписания для указанных групп
        for find in group_names:
            qs = self.queryset.filter(
                Q(group__name__contains=find) | Q(room__number__contains=find) | Q(teacher__name__contains=find))
            schedule_content += self.service().get_timetable_html(qs)

        # # Ниже приведен пример генерации расписания в виде текстового файла
        # schedule_content = "Расписание для групп: {}\n".format(", ".join(group_names))
        # schedule_content += "...\n"  # Здесь должны быть реальные данные расписания

        # Создание и возврат файла в ответе
        response = HttpResponse(schedule_content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="schedule.html"'
        return response


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
