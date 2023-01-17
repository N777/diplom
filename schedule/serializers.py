from rest_framework import serializers

from schedule.models import Timetable


class TimetableSerializer(serializers.ModelSerializer):
    """Транзакции."""

    class Meta:
        model = Timetable
        fields = '__all__'
