import sys
from functools import wraps
from json import dumps
from urllib.parse import parse_qs


def log_call(func):
    @wraps(func)
    def wrapper(params):
        status_code, response_body = func(params)
        log_entry = {
            "handler": func.__name__,
            "params": params,
            "response": [status_code, response_body],
        }
        print(dumps(log_entry))
        return status_code, response_body

    return wrapper


@log_call
def home_handler(params):
    return 200, "Home Page"


@log_call
def admin_handler(params):
    return 200, "Admin Panel"


@log_call
def user_handler(params):
    # Если name нет — возвращаем 403, как в тестах
    if "name" not in params:
        return 403, "Forbidden"
    return 200, f"Hello, {params['name']}!"


@log_call
def attempt_handler(params):
    # Если name нет — возвращаем 403, как в тестах
    if "name" not in params:
        return 403, "Forbidden"
    return (
        200,
        f"Good try, {params['name']}! Your attempt on task '{params.get('task', 'unknown')}' is accepted!",
    )


@log_call
def not_found_handler(params):
    return 404, "Not Found"


def router(path):
    if path == "/":
        return home_handler
    elif path.startswith("/user"):
        return user_handler
    elif path.startswith("/attempt"):
        return attempt_handler
    elif path.startswith("/admin"):
        return admin_handler
    else:
        return not_found_handler


def wsgi_server():
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


app = wsgi_server()
app.send(None)

for request in sys.stdin:
    app.send(request.strip())
