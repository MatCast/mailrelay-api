from requests.exceptions import ConnectionError


def check_request(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    return wrapper
