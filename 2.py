from html.parser import HTMLParser
import json

class ScheduleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_row = False
        self.in_header = False
        self.in_data = False
        self.current_row = []
        self.headers = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.in_table = True
        if self.in_table:
            if tag == 'tr':
                self.in_row = True
                self.current_row = []
            elif tag == 'th':
                self.in_header = True
            elif tag == 'td':
                self.in_data = True

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
        if self.in_table:
            if tag == 'tr':
                if self.current_row:
                    if self.headers:
                        self.rows.append(self.current_row)
                    else:
                        self.headers = self.current_row
                self.in_row = False
            elif tag == 'th':
                self.in_header = False
            elif tag == 'td':
                self.in_data = False

    def handle_data(self, data):
        if self.in_header or self.in_data:
            self.current_row.append(data.strip())

# HTML-код
html_content = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Расписание на понедельник</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #000;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Расписание пар на понедельник</h1>
    <table>
        <tr>
            <th>Время</th>
            <th>Предмет</th>
            <th>Формат</th>
            <th>Преподаватель</th>
            <th>Место проведения</th>
        </tr>
        <tr>
            <td>11:40 - 13:10</td>
            <td>Программирование</td>
            <td>Лабораторная работа</td>
            <td>Абузов Ярослав Александрович</td>
            <td>Аудитория 2117, Кронверский 49</td>
        </tr>
        <tr>
            <td>13:30 - 15:00</td>
            <td>Программирование</td>
            <td>Лабораторная работа</td>
            <td>Абузов Ярослав Александрович</td>
            <td>Аудитория 2117, Кронверский 49</td>
        </tr>
        <tr>
            <td>15:20 - 16:50</td>
            <td>Линейная алгебра</td>
            <td>Лекция</td>
            <td>Карпов Дмитрий Валерьевич</td>
            <td>Аудитория 1404, Кронверский 49</td>
        </tr>
        <tr>
            <td>17:00 - 18:30</td>
            <td>Линейная алгебра</td>
            <td>Практическое занятие</td>
            <td>Карпов Дмитрий Валерьевич</td>
            <td>Аудитория 1404, Кронверский 49</td>
        </tr>
    </table>
</body>
</html>
'''

# Создание экземпляра парсера и разбор HTML
parser = ScheduleParser()
parser.feed(html_content)

# Построение списка словарей для JSON
schedule = []
for row in parser.rows:
    entry = dict(zip(parser.headers, row))
    schedule.append(entry)

# Вывод результата в формате JSON
print(json.dumps(schedule, ensure_ascii=False, indent=4))