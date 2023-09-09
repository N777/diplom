import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from rest_framework.exceptions import ValidationError

User = get_user_model()


class NumbersOfWeek(models.IntegerChoices):
    ODD = 1, 'Нечётная'
    EVEN = 0, 'Чётная'


class Lesson(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.number


class WeekDays(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LessonsTimes(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    @staticmethod
    def get_lesson_number(need_time: datetime.time):
        lessons_times = list(LessonsTimes.objects.all())
        for i in range(len(lessons_times)):
            times = lessons_times[i].start_time
            try:
                next_times = lessons_times[i + 1].start_time
            except IndexError:
                next_times = lessons_times[i].end_time
            if times <= need_time < next_times:
                return lessons_times[i].id
        raise ValidationError("Ошибка определения в расписании времени проведения")


class Timetable(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)
    lesson_type = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, null=True)
    subgroup = models.IntegerField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, null=True)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    day = models.ForeignKey(WeekDays, on_delete=models.DO_NOTHING)
    week = models.IntegerField(choices=NumbersOfWeek.choices)
    lesson_number = models.ForeignKey(LessonsTimes, validators=[MinValueValidator(1), MaxValueValidator(8)],
                                      on_delete=models.DO_NOTHING)
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    once = models.BooleanField(default=False, null=False)

    def clean(self):
        if not self.lesson_number and not (self.start_time or self.end_time):
            raise ValidationError("Должно быть заполнено или пара или время начало и конца занятия")

    def __str__(self):
        return f"{self.lesson_type}-{self.lesson.name}-{self.group.name}-{self.teacher.name}" \
               f"-{self.lesson_number.id} пара"
