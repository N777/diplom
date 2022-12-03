import pandas


class TimetableParseService:

    ULSTU_TIMETABLE_URL = fr'https://lk.ulstu.ru/timetable/shared/schedule/%D0%A7%D0%B0%D1%81%D1%82%D1%8C%202%20%E2%80%93%20%D0%A4%D0%98%D0%A1%D0%A2,%20%D0%A1%D0%A4,%20%D0%93%D0%A4/%s.html'

    def empty_list(self):
        arr = [""] * 7
        for i in range(7):
            arr[i] = [""] * 9
        return arr

    def parse_timetable_from_html(self):

        cabinets = {}
        cabinet_list = [*range(305, 315), 423]

        for i in cabinet_list:
            cabinets.update({i: {0: self.empty_list(), 1: self.empty_list()}})

        for counter in range(1, 100):
            print(counter)
            url = self.ULSTU_TIMETABLE_URL % counter
            tables = pandas.read_html(url, header=1, index_col=0)
            for room in cabinet_list:
                for week in range(2):
                    for x in range(len(tables[week])):
                        tables_week = tables[week].values
                        for y in range(len(tables_week[x])):
                            tables_week_x = tables_week[x]
                            if isinstance(tables_week_x[y], str) and f"3-{room}" in tables_week_x[y]:
                                cabinets[room][week][x][y] = tables_week_x[y]

    @classmethod
    def cabinets_to_html(cls, rooms):
        result = ''
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        for room in range(305, 315):
            for week in range(2):
                result += f"<p>{room} Неделя {week + 1}</p>"
                temp = pandas.DataFrame(rooms[room][week], dtype='string', columns=[i for i in range(1, 10)], index=days)
                temp = temp.drop(['Воскресенье'], axis=0).drop([9], axis=1)
                result += temp.to_html(justify='center')
        with open("time.html", mode='w') as file:
            file.write(result)