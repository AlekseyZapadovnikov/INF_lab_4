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

# Функция для извлечения текста между тегами
def get_text_between_tags(s, start_tag, end_tag):
    result = []
    start = 0
    while True:
        start_index = s.find(start_tag, start)
        if start_index == -1:
            break
        start_index += len(start_tag)
        end_index = s.find(end_tag, start_index)
        if end_index == -1:
            break
        result.append(s[start_index:end_index].strip())
        start = end_index + len(end_tag)
    return result

# Извлечение заголовков таблицы
headers = get_text_between_tags(html_content, '<th>', '</th>')

# Извлечение строк таблицы
rows_raw = html_content.split('<tr>')[2:]  # Пропускаем заголовок таблицы
rows = []
for row_raw in rows_raw:
    cells = get_text_between_tags(row_raw, '<td>', '</td>')
    rows.append(cells)

# Построение списка словарей
schedule = []
for row in rows:
    entry = {}
    for i in range(len(headers)):
        entry[headers[i]] = row[i]
    schedule.append(entry)

# Преобразование в формат JSON
json_output = '[\n'
for i, entry in enumerate(schedule):
    json_output += '    {\n'
    for j, key in enumerate(headers):
        json_output += f'        "{key}": "{entry[key]}"'
        if j < len(headers) - 1:
            json_output += ',\n'
        else:
            json_output += '\n'
    if i < len(schedule) - 1:
        json_output += '    },\n'
    else:
        json_output += '    }\n'
json_output += ']'

# Вывод результата
print(json_output)


html_content = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Расписание на вторник</title>
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
    <h1>Расписание пар на вторник</h1>
    <table>
        <tr>
            <th>Время</th>
            <th>Предмет</th>
            <th>Формат</th>
            <th>Преподаватель</th>
            <th>Место проведения</th>
        </tr>
        <tr>
            <td>17:00 - 18:30</td>
            <td>Дискретка</td>
            <td>Лекция</td>
            <td>Дмитрий Валерьевич Карпов</td>
            <td>Аудитория 1419, Кронверский 49</td>
        </tr>
        <tr>
            <td>18:40 - 20:10</td>
            <td>Дискретка</td>
            <td>Практика</td>
            <td>Миша</td>
            <td>Аудитория 2308, Кронверский 49</td>
        </tr>
    </table>
</body>
</html>
'''