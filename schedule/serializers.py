from datetime import datetime
from enum import Enum

from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError, ValidationError

from schedule.models import Timetable, Group, WeekDays, NumbersOfWeek, Lesson, Teacher, Room, LessonsTimes


class TimetableSerializer(serializers.ModelSerializer):
    """Транзакции."""

    lesson = serializers.SlugRelatedField(queryset=Lesson.objects.all(), slug_field='name')
    group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name')
    teacher = serializers.SlugRelatedField(queryset=Teacher.objects.all(), slug_field='name')
    room = serializers.SlugRelatedField(queryset=Room.objects.all(), slug_field='number')
    day = serializers.SlugRelatedField(queryset=WeekDays.objects.all(), slug_field='name')
    lesson_number = serializers.SlugRelatedField(queryset=LessonsTimes.objects.all(), slug_field='id')
    week = serializers.ChoiceField(choices=[(x.value, x.name) for x in NumbersOfWeek])

    class Meta:
        model = Timetable
        fields = '__all__'


class EventTimetableSerializer(serializers.ModelSerializer):
    """Расписание мероприятия"""

    lesson = serializers.CharField()
    room = serializers.SlugRelatedField(queryset=Room.objects.all(), slug_field='number')
    date = serializers.DateField(required=True)
    start_time = serializers.TimeField(required=True)
    end_time = serializers.TimeField(required=True)

    class Meta:
        model = Timetable
        fields = ('id', 'lesson', 'room', 'start_time', 'end_time', 'date', 'once')

    @transaction.atomic()
    def create(self, validated_data):
        lesson, _ = Lesson.objects.get_or_create(name=validated_data.get('lesson'))
        day = validated_data.get('date').weekday() + 1
        week = int(validated_data.get('date').strftime('%U')) - int(
            validated_data.get('date').replace(day=1).strftime('%U'))
        start_lesson_number = LessonsTimes.get_lesson_number(validated_data.get('start_time'))
        end_lesson_number = LessonsTimes.get_lesson_number(validated_data.get('end_time'))
        timetable = None
        for lesson_number in range(start_lesson_number, end_lesson_number + 1):
            timetable = Timetable(
                lesson=lesson,
                lesson_type='event',
                room=validated_data.get('room'),
                day=WeekDays.objects.get(id=day),
                week=week % 2,
                lesson_number=LessonsTimes.objects.get(id=lesson_number),
                date=validated_data.get('date'),
                start_time=validated_data.get('start_time'),
                end_time=validated_data.get('end_time'),
                once=validated_data.get('once')
            )
            timetable.save()
        if not timetable:
            raise ValidationError
        return timetable


class LessonTimetableSerializer(serializers.ModelSerializer):
    """Расписание занятия"""

    lesson = serializers.SlugRelatedField(queryset=Lesson.objects.all(), slug_field='name')
    group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name')
    teacher = serializers.SlugRelatedField(queryset=Teacher.objects.all(), slug_field='name')
    room = serializers.SlugRelatedField(queryset=Room.objects.all(), slug_field='number')
    day = serializers.SlugRelatedField(queryset=WeekDays.objects.all(), slug_field='name')
    lesson_number = serializers.SlugRelatedField(queryset=LessonsTimes.objects.all(), slug_field='id')
    week = serializers.ChoiceField(choices=[(x.value, x.name) for x in NumbersOfWeek])

    class Meta:
        model = Timetable
        fields = ('id', 'lesson', 'group', 'teacher', 'room', 'day', 'week', 'lesson_number', 'once')


class WeekDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDays
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return instance.name

    class Meta:
        model = Group
        fields = ('name',)


class TeacherSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return instance.name

    class Meta:
        model = Teacher
        fields = ('name',)


class RoomSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return instance.number

    class Meta:
        model = Room
        fields = ('number',)


class LessonSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return instance.name

    class Meta:
        model = Lesson
        fields = ('name',)


class LessonsTimesSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(format="%H:%M", read_only=True)
    end_time = serializers.TimeField(format="%H:%M", read_only=True)

    class Meta:
        model = LessonsTimes
        fields = '__all__'
