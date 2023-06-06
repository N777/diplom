import re
from dataclasses import dataclass
from itertools import groupby
from typing import List

import requests
from django.db.models import QuerySet
from django.template.loader import render_to_string

from schedule.models import Timetable, Lesson, Room, Teacher, Group, WeekDays, NumbersOfWeek, LessonsTimes
from schedule.views import TimetableViewSet

LESSON_TYPES = {
    'пр': 'practice',
    'Лаб': 'laboratory',
    'лек': 'lecture',
    'экз': 'exam'
}


@dataclass
class ApiLesson:
    name_lesson: str = None
    type_lesson: str = None
    group: str = None
    subgroup: int = None
    teacher: str = None
    room: str = None


@dataclass
class ApiTimetable:
    lesson: ApiLesson = None
    day: int = None
    week: str = None
    lesson_number: str = None


class TimetableParseService:
    session = requests.Session()

    def auth_on_ulstu(self):
        log_data = {
            'login': 'egorov.v',
            'password': '3c817f04'
        }
        self.session.post('https://lk.ulstu.ru/?q=auth/login', data=log_data)

    def get_groups(self) -> dict:
        base_url = 'https://time.ulstu.ru/api/1.0/groups'
        response = self.session.get(base_url)
        return response.json()

    def get_timetable_by_group(self, group: str):
        base_url = 'https://time.ulstu.ru/api/1.0/timetable'
        response = self.session.get(base_url, params={'filter': group})
        return response.json()

    def parse_timetable(self, timetable):
        temp_timetable = ApiTimetable()
        for number_week, week in timetable['weeks'].items():
            temp_timetable.week = number_week
            for day in week['days']:
                temp_timetable.day = day['day']
                for lesson_number, lesson in enumerate(day['lessons']):
                    if not lesson:
                        continue
                    temp_timetable.lesson_number = lesson_number
                    temp_timetable.lesson = self.parse_lesson(lesson[0])
                    self.save_timetable_to_db(temp_timetable)

    def save_timetable_to_db(self, timetable: ApiTimetable):
        lesson, created = Lesson.objects.get_or_create(name=timetable.lesson.name_lesson)
        room, created = Room.objects.get_or_create(number=timetable.lesson.room)
        teacher, created = Teacher.objects.get_or_create(name=timetable.lesson.teacher)
        group, created = Group.objects.get_or_create(name=timetable.lesson.group)
        day = WeekDays.objects.get(id=timetable.day + 1)
        lesson_number = LessonsTimes.objects.get(id=int(timetable.lesson_number) + 1)
        Timetable.objects.create(
            lesson=lesson,
            lesson_type=timetable.lesson.type_lesson,
            group=group,
            subgroup=timetable.lesson.subgroup,
            teacher=teacher,
            room=room,
            day=day,
            week=int(timetable.week) % 2,
            lesson_number=lesson_number
        )

    def parse_lesson(self, lesson: dict) -> ApiLesson:
        type_lesson, name_lesson = lesson['nameOfLesson'].split('.')
        find_subgroup = re.search(r'\D+- +\d', name_lesson)
        subgroup = None
        if find_subgroup:
            name_lesson = find_subgroup
            subgroup = int(name_lesson[0][-1])
            name_lesson = name_lesson[0][:-3]
        # name_lesson, subgroup = name_lesson.split('-') #TODO учесть кейс 2 тире "тайм-менеджмент- 2 п/г"
        return ApiLesson(
            name_lesson=name_lesson,
            type_lesson=LESSON_TYPES[type_lesson],
            group=lesson['group'],
            subgroup=subgroup,
            room=lesson['room'],
            teacher=lesson['teacher'],
        )


class TimetablePrintService:

    def __init__(self):
        week_days = list(WeekDays.objects.all().values('name'))
        self.week_day = {key + 1: item['name'] for key, item in enumerate(week_days)}

    def _group_by_key(self, items: List[dict], key: str) -> dict:
        grouped_data = {}
        for item in items:
            category = item[key]
            if category in grouped_data:
                grouped_data[category].append(item)
            else:
                grouped_data[category] = [item]
        return grouped_data

    def get_timetable_html(self, query_set: QuerySet):
        for i, week in NumbersOfWeek.choices:
            week_queryset = query_set.filter(week=i)
            self.get_week_timetable_html(week_queryset, week)

    def get_week_timetable_html(self, query_set: QuerySet, week: str):
        query_set = query_set.order_by('day_id')
        data = list(query_set.values('lesson__name', 'group__name', 'lesson_number_id', 'room__number', 'teacher__name',
                                     'lesson_type', 'day_id'))
        grouped_data = self._group_by_key(data, 'day_id')
        for key, item in grouped_data.items():
            grouped_item = self._group_by_key(item, 'lesson_number_id')
            grouped_data[key] = grouped_item
        data = {'table': grouped_data,
                'week': week,
                'week_days': self.week_day,
                'day_iterator': range(1, 8),
                'lesson_iterator': range(1, 9)}

        temp = render_to_string('timetable.html', context=data)
        return temp
