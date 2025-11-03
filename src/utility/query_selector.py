from playwright.async_api import ElementHandle

async def query_selector(element: ElementHandle, query: str):
    """
    Query a single element within a given Playwright ElementHandle and ensure
    that an element is found.

    Args:
        element: The Playwright ElementHandle to query within.
        query: The CSS selector string to match the element.

    Raises:
        Exception: If no element is found (i.e., query returns None).

    Returns:
        The ElementHandle object matching the selector.
    """
    result = await element.query_selector(query)

    if result is None:
        raise Exception(f"Error: searched '{query}', received None.")

    return result