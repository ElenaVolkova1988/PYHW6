import argparse
from task1 import date_func

parser = argparse.ArgumentParser(description='Проверка даты')
parser.add_argument('date', type=str, help='Дата в формате ДД.ММ.ГГГГ')

args = parser.parse_args()

if date_func(args.date):
    print(f'Дата {args.date} существует')
else:
    print(f'Дата {args.date} не существует')