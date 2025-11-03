from playwright.async_api import ElementHandle

async def query_selector_all(element: ElementHandle, query: str, required_length: int = 1):
    """
    Query multiple elements within a given Playwright ElementHandle and ensure
    that a minimum number of elements are found.

    Args:
        element: The Playwright ElementHandle to query within.
        query: The CSS selector string to match elements.
        required_length: Minimum number of elements expected (default is 1).

    Raises:
        Exception: If fewer elements than `required_length` are found.

    Returns:
        A list of ElementHandle objects matching the selector.
    """
    result = await element.query_selector_all(query)

    if len(result) < required_length:
        raise Exception(f"Error: expected at least {required_length} element(s) from '{query}', received {len(result)}.")

    return result