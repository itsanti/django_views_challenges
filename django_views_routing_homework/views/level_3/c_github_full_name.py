"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут: https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""

from http import HTTPStatus
from django.http import HttpResponse, HttpRequest, JsonResponse
import requests

def fetch_name_from_github_view(request: HttpRequest, github_username: str) -> HttpResponse:
    r = requests.get(f'https://api.github.com/users/{github_username}')
    if r.status_code == HTTPStatus.NOT_FOUND:
        return JsonResponse(data={}, status=HTTPStatus.NOT_FOUND)
    data = r.json()
    return JsonResponse(data={'name': data.get('name', None)})
