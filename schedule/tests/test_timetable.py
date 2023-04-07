from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from schedule.models import Group, Lesson, NumbersOfWeek, Room, Teacher, Timetable, WeekDays
from schedule.serializers import TimetableSerializer


class TimetableViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.lesson = Lesson.objects.create(name='Math')
        self.group = Group.objects.create(name='Group A')
        self.teacher = Teacher.objects.create(name='John Doe')
        self.room = Room.objects.create(number='101')
        self.day = WeekDays.objects.create(name='Monday')
        self.timetable = Timetable.objects.create(
            lesson=self.lesson,
            lesson_type='lecture',
            group=self.group,
            subgroup=1,
            teacher=self.teacher,
            room=self.room,
            day=self.day,
            week=0,
            lesson_number=1
        )
        self.valid_payload = {
            'lesson': 'Math',
            'lesson_type': 'lecture',
            'group': 'Group A',
            'subgroup': 1,
            'teacher': 'John Doe',
            'room': '101',
            'day': 'Monday',
            'week': 0,
            'lesson_number': 1
        }
        self.invalid_payload = {
            'lesson': 'Biology',
            'lesson_type': 'lecture',
            'group': 'Group B',
            'subgroup': 1,
            'teacher': 'Jane Doe',
            'room': '102',
            'day': 'Tuesday',
            'week': 1,
            'lesson_number': 10
        }

    def test_get_all_timetables(self):
        response = self.client.get(reverse('timetable-list'))
        timetables = Timetable.objects.all()
        serializer = TimetableSerializer(timetables, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_timetable(self):
        response = self.client.get(reverse('timetable-detail', kwargs={'pk': self.timetable.id}))
        timetable = Timetable.objects.get(pk=self.timetable.id)
        serializer = TimetableSerializer(timetable)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_timetable(self):
        response = self.client.get(reverse('timetable-detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_timetable(self):
        response = self.client.post(
            reverse('timetable-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_timetable(self):
        response = self.client.post(
            reverse('timetable-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_timetable(self):
        response = self.client.put(
            reverse('timetable-detail', kwargs={'pk': self.timetable.id}),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_timetable(self):
        response = self.client.put(
            reverse('timetable-detail', kwargs={'pk': self.timetable.id}),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
