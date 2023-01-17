from django.urls import path, include
from rest_framework import routers

from diplom import settings
from schedule import views

router = routers.SimpleRouter()
router.include_root_view = settings.DEBUG
router.register(r'api/timetable', views.TimetableViewSet,
                basename='timetable')


urlpatterns = [
    # path('', index, name='index'),
    path('', include(router.urls))
]
