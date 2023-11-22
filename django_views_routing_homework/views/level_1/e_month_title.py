import locale
from datetime import date

from django.http import HttpResponse, HttpResponseNotFound

"""
Вьюха get_month_title_view возвращает название месяца по его номеру. 
Вся логика работы должна происходить в функции get_month_title_by_number.

Задания:
    1. Напишите логику получения названия месяца по его номеру в функции get_month_title_by_number
    2. Если месяца по номеру нет, то должен возвращаться ответ типа HttpResponseNotFound c любым сообщением об ошибке
    3. Добавьте путь в файле urls.py, чтобы при открытии http://127.0.0.1:8000/month-title/тут номер месяца/ 
       вызывалась вьюха get_month_title_view. Например http://127.0.0.1:8000/month-title/3/ 
"""


def get_month_title_by_number(month_number: int) -> HttpResponse:
    loc = locale.getlocale()
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    try:
        return HttpResponse(date(1970, month_number, 1).strftime("%B"))
    except ValueError:
        return HttpResponseNotFound('Месяца с таким номером не существует')


def get_month_title_view(request, month_number: int) -> HttpResponse:
    return get_month_title_by_number(month_number)
