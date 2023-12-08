"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""
import json
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseNotAllowed
from http import HTTPStatus
from typing import TypedDict
from typing_extensions import NotRequired
import enum
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class RegisteredFrom(enum.Enum):
    WEBSITE = 'website'
    MOBILE_APP = 'mobile_app'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class User(TypedDict):
    full_name: str
    email: str
    registered_from: RegisteredFrom
    age: NotRequired[int]


def is_valid_user_data(user: User):
    if (len(user.keys()) > 4 or
            len(set(user.keys()).intersection(set(['full_name', 'email', 'registered_from']))) != 3):
        return False
    if any([type(user['full_name']) != str, type(user['email']) != str, type(user['registered_from']) != str]):
        return False
    if len(user['full_name']) < 5 or len(user['full_name']) > 256:
        return False
    try:
        validate_email(user['email'])
    except ValidationError as e:
        return False
    if not RegisteredFrom.has_value(user['registered_from']):
        return False
    if type(user.get('age', 0)) != int:
        return False
    return True

def validate_user_data_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        try:
            data: User = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return JsonResponse(data={}, status=HTTPStatus.BAD_REQUEST)
        return JsonResponse(data={"is_valid": is_valid_user_data(data)})
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])
