"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""
import random
import string
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden


def text_generator(length):
    return ''.join(random.choice(string.ascii_letters + ' ,.!?') for _ in range(length))

def generate_file_with_text_view(request: HttpRequest) -> HttpResponse:
    FILE_SIZE_LIMIT = (1, 1024)
    length = request.GET.get('length', '')
    try:
        length = int(length)
    except ValueError:
        return HttpResponseForbidden()
    if length < FILE_SIZE_LIMIT[0] or length > FILE_SIZE_LIMIT[1]:
        return HttpResponseForbidden()

    headers = {
        "Content-Type": "text/plain",
        "Content-Disposition": 'attachment; filename="generated.txt"'
    }
    return HttpResponse(text_generator(length), headers=headers)
