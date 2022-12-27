import pandas
import requests

class TimetableParseService:

    def auth_on_ulstu(self):
        log_data = {
            'login': '',
            'password': ''
        }
        response = requests.post('https://lk.ulstu.ru/?q=auth/login', data=log_data)
        assert response.status_code

    def get_timetable(self):
        base_url = 'https://time.ulstu.ru/api/1.0/timetable'


service = TimetableParseService()
service.auth_on_ulstu()
service
