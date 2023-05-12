from enum import Enum

from rest_framework import serializers

from schedule.models import Timetable, Group, WeekDays, NumbersOfWeek, Lesson, Teacher, Room


class TimetableSerializer(serializers.ModelSerializer):
    """Транзакции."""

    lesson = serializers.SlugRelatedField(queryset=Lesson.objects.all(), slug_field='name')
    group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name')
    teacher = serializers.SlugRelatedField(queryset=Teacher.objects.all(), slug_field='name')
    room = serializers.SlugRelatedField(queryset=Room.objects.all(), slug_field='number')
    day = serializers.SlugRelatedField(queryset=WeekDays.objects.all(), slug_field='name')
    week = serializers.ChoiceField(choices=[(x.value, x.name) for x in NumbersOfWeek])

    class Meta:
        model = Timetable
        fields = '__all__'


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
