from django.core.management.base import BaseCommand

from schedule.models import Timetable
from schedule.services import TimetableParseService


class Command(BaseCommand):

    def handle(self, *args, **options):
        service = TimetableParseService()
        service.auth_on_ulstu()
        groups = service.get_groups().get('response')
        need_groups = list(filter(lambda group: 'ИВТ' in group, groups))
        Timetable.objects.all().delete()
        for group in need_groups:
            timetable = service.get_timetable_by_group(group)
            service.parse_timetable(timetable['response'])
            print(timetable)
