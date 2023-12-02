from django.http import HttpResponse


"""
Вьюха greet_user_in_different_languages_view приветствует пользователя в зависимости от имени и языка в пути, если
язык не русский и не английский, то приветствуем просто смайликом.

Задания:
    1. Сама логика во вьюхе написана, внимательно изучите ее.
    2. Откройте urls.py и создайте путь, который будет обрабатывать эту вьюху, чтобы при открытии
       http://127.0.0.1:8000/greet/misha/en/ успешно вызывалась вьюха greet_user_in_different_languages.
       Подсказка как это сделать тут https://docs.djangoproject.com/en/4.2/topics/http/urls/#example
    3. Поэксперементируйте с разными именами и языками, чтобы убедться что все работает как вы ожидаете.
"""


def greet_user_in_different_languages_view(request, name: str, language: str):
    titled_name = name.title()
    headers = {
        'Content-Language': 'en-US',
    }

    if language == 'ru':
        response_content = f'Привет, {titled_name}'
        headers['Content-Language'] = 'ru-RU'
    elif language == 'en':
        response_content = f'Hello, {titled_name}'
    else:
        response_content = f'👋, {titled_name}'


    return HttpResponse(response_content, headers=headers)
