from django.urls import path, include
from rest_framework import routers

from diplom import settings
from schedule import views

router = routers.SimpleRouter()
router.include_root_view = settings.DEBUG
router.register(r'timetable', views.TimetableViewSet,
                basename='timetable')
router.register(r'event-timetable', views.EventTimetableViewSet,
                basename='event-timetable')
router.register(r'lesson-timetable', views.LessonTimetableViewSet,
                basename='lesson-timetable')
router.register(r'group', views.GroupViewSet, basename='group')
router.register(r'room', views.RoomViewSet, basename='room')
router.register(r'teacher', views.TeacherViewSet, basename='teacher')
router.register(r'lesson', views.LessonViewSet, basename='lesson')
router.register(r'lessons-times', views.LessonsTimesViewSet, basename='lesson')


urlpatterns = [
    # path('', index, name='index'),
    path('', include(router.urls))
]
