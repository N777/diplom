from django.urls import path, include
from rest_framework import routers

from diplom import settings
from schedule import views

router = routers.SimpleRouter()
router.include_root_view = settings.DEBUG
router.register(r'api/timetable', views.TimetableViewSet,
                basename='timetable')
router.register(r'api/group', views.GroupViewSet, basename='group')


urlpatterns = [
    # path('', index, name='index'),
    path('', include(router.urls))
]
