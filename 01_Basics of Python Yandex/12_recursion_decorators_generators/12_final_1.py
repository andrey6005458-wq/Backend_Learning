import sys
from urllib.parse import parse_qs


# Handler'ы для разных маршрутов
def home_handler(params):
    return 200, "Home Page"


def admin_handler(params):
    return 200, "Admin Panel"


def user_handler(params):
    return 200, f"Hello, {params['name']}!"


def attempt_handler(params):
    return (
        200,
        f"Good try, {params['name']}! Your attempt on task '{params['task']}' is accepted!",
    )


def not_found_handler(params):
    return 404, "Not Found"


# Функция маршрутизации
def router(path):
    if path == "/":
        return home_handler
    elif path.startswith("/user"):
        return user_handler
    elif path.startswith("/attempt"):
        return attempt_handler
    elif path.startswith("/admin"):
        return admin_handler
    return not_found_handler


# WSGI-сервер (генератор)
def wsgi_server():
    """Обрабатывает запросы и возвращает каждый из ответов через yield"""
    request = yield None

    while True:
        parts = request.split()
        if len(parts) < 2:
            request = yield (400, "Bad Request")
            continue

        method, url = parts[0], parts[1]

        if "?" in url:
            path, query_string = url.split("?", 1)
            params = {k: v[0] for k, v in parse_qs(query_string).items()}
        else:
            path = url
            params = {}

        handler = router(path)
        status_code, response_body = handler(params)

        request = yield (status_code, response_body)


# Имитация работы сервера
app = wsgi_server()
app.send(None)

for request in sys.stdin:
    print(app.send(request.strip()))
