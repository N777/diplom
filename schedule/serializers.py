from rest_framework import serializers

from schedule.models import Timetable


class TimetableSerializer(serializers.ModelSerializer):
    """Транзакции."""

    lesson_name = serializers.CharField(source='lesson.name')
    group_name = serializers.CharField(source='group.name')
    teacher_name = serializers.CharField(source='teacher.name')
    room_number = serializers.CharField(source='room.number')

    class Meta:
        model = Timetable
        fields = ['lesson_name', 'lesson_type', 'subgroup', 'group_name', 'teacher_name', 'room_number', 'day', 'week', 'lesson_number']
