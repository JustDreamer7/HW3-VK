from datetime import datetime


def app(environ, start_response):
    url = str(environ['wsgi.url_scheme']) + '://' + str(environ["SERVER_NAME"]) + ":" + str(environ["SERVER_PORT"]),
    str(environ["PATH_INFO"])

    time = str(datetime.now(tz=None))
    data = {'url': url, 'time': time}

    data = bytes(str(data), 'utf-8')

    start_response("200 OK",
                   [("Content-Type", "text/plain"),
                    ("Content-Length", str(len(data)))])

    return iter([data])


if __name__ == "__main__":
    app(1, 1)
