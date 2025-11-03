from typing import Callable


def error_search_url(func: Callable, expected_url: str, actual_url: str):
    return f"'{func.__name__}' call failed: expected {expected_url} in url, received {actual_url}."
