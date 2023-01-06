from dataclasses import dataclass

import requests

from schedule.models import Timetable, Lesson, Room, Teacher, Group


@dataclass
class ApiLesson:
    name_lesson: str = None
    group: str = None
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
        Timetable.objects.create(
            lesson=lesson,
            group=group,
            teacher=teacher,
            room=room,
            day=timetable.day,
            week=int(timetable.week) % 2,
            lesson_number=timetable.lesson_number
        )

    def parse_lesson(self, lesson: dict) -> ApiLesson:
        return ApiLesson(
            name_lesson=lesson['nameOfLesson'],
            group=lesson['group'],
            room=lesson['room'],
            teacher=lesson['teacher'],
        )
