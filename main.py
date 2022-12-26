from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from dateutil.relativedelta import relativedelta
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

now = date.today()
start_date = date(1920, 1, 1)
delta = relativedelta(now, start_date)


def ending(number):
    number = number % 100
    if 21 > number > 4:
        return 'лет'

    number = number % 10

    if number == 1:
        return 'год'
    if 1 < number < 5:
        return 'года'
    return 'лет'


excel_data_df = pandas.read_excel('wines_table.xlsx', sheet_name='Лист1', keep_default_na=False)
wines = excel_data_df.to_dict(orient='records')
wines_by_cat = {}

for wine in wines:
    wines_by_cat.setdefault(wine['Категория'], []).append(wine)

rendered_page = template.render(
    wines=wines_by_cat,
    year=delta.years,
    end=ending(delta.years)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
