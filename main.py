import argparse
from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from dateutil.relativedelta import relativedelta
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_year_ending(number):
    number = number % 100
    if 21 > number > 4:
        return 'лет'

    number = number % 10

    if number == 1:
        return 'год'
    if 1 < number < 5:
        return 'года'
    return 'лет'


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    now = date.today()
    start_date = date(1920, 1, 1)
    delta = relativedelta(now, start_date)

    parser = argparse.ArgumentParser(description='Load products list to server')
    parser.add_argument('filename', type=str, help='Specify path to the file')
    parser.add_argument('listname', type=str, help='Specify page of excel file')
    args = parser.parse_args()
    excel_data_df = pandas.read_excel(args.filename, sheet_name=args.listname, keep_default_na=False)
    wines = excel_data_df.to_dict(orient='records')
    wines_by_cat = {}

    for wine in wines:
        wines_by_cat.setdefault(wine['Категория'], []).append(wine)

    rendered_page = template.render(
        wines=wines_by_cat,
        year=delta.years,
        end=get_year_ending(delta.years)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
