from django.core.management.base import BaseCommand, CommandError

from schedule.models import Timetable, NumbersOfWeek
from schedule.services import TimetableParseService, TimetablePrintService


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        queryset = Timetable.objects.filter(once=False)
        service = TimetablePrintService()
        service.get_timetable_html(queryset)
