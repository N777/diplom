from django.core.management.base import BaseCommand

from schedule.models import Timetable
from schedule.services import TimetableParseService


class Command(BaseCommand):

    def handle(self, *args, **options):
        service = TimetableParseService()
        service.reset_timetable()
