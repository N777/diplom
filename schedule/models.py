from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class NumbersOfWeek(models.IntegerChoices):
    EVEN = 0, 'Чётная'
    ODD = 1, 'Нечётная'


class DaysOfWeek(models.IntegerChoices):
    Monday = 0, 'Понедельник'
    Tuesday = 1, 'Вторник'
    Wednesday = 2, 'Среда'
    Thursday = 3, 'Четверг'
    Friday = 4, 'Пятница'
    Saturday = 5, 'Суббота'
    Sunday = 6, 'Воскресенье'


class Lesson(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)

    def get_or_create(self, name: str):
        try:
            object = Group.objects.get(name=name)
        except Group.DoesNotExist:
            object = Group.objects.create(name=name)
        return object

    def __str__(self):
        return self.name


class Teacher(models.Model):
    # TODO сделать наследование от User
    name = models.CharField(max_length=255)

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


class Timetable(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)
    lesson_type = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    subgroup = models.IntegerField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    day = models.ForeignKey(WeekDays, on_delete=models.DO_NOTHING)
    week = models.IntegerField(choices=NumbersOfWeek.choices)
    lesson_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)])

    def __str__(self):
        return f"{self.lesson_type}-{self.lesson.name}-{self.group.name}-{self.teacher.name}-{self.lesson_number+1} пара"
