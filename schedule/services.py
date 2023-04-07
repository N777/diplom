import re
from dataclasses import dataclass

import requests

from schedule.models import Timetable, Lesson, Room, Teacher, Group, WeekDays

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
        Timetable.objects.create(
            lesson=lesson,
            lesson_type=timetable.lesson.type_lesson,
            group=group,
            subgroup=timetable.lesson.subgroup,
            teacher=teacher,
            room=room,
            day=day,
            week=int(timetable.week) % 2,
            lesson_number=timetable.lesson_number
        )

    def parse_lesson(self, lesson: dict) -> ApiLesson:
        type_lesson, name_lesson = lesson['nameOfLesson'].split('.')
        find_subgroup = re.search(r'\D+- +\d', name_lesson)
        subgroup = None
        if find_subgroup:
            name_lesson = find_subgroup
            subgroup = int(name_lesson[0][-1])
            name_lesson = name_lesson[0][:-3]
        #name_lesson, subgroup = name_lesson.split('-') #TODO учесть кейс 2 тире "тайм-менеджмент- 2 п/г"
        return ApiLesson(
            name_lesson=name_lesson,
            type_lesson=LESSON_TYPES[type_lesson],
            group=lesson['group'],
            subgroup=subgroup,
            room=lesson['room'],
            teacher=lesson['teacher'],
        )
