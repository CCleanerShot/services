def error_search_url(expected_url: str, actual_url: str):
    """
    Return a formatted error message indicating that the expected URL
    was not found in the actual URL.

    Args:
        expected_url: The URL or substring that was expected.
        actual_url: The URL that was actually received.

    Returns:
        A descriptive error message showing the expected and actual URLs.
    """
    return f"Expected {expected_url} in url, received {actual_url}."