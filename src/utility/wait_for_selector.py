from playwright.async_api import ElementHandle

async def wait_for_selector(element: ElementHandle, query: str):
    """
    Wait for a specific element to appear within a given Playwright ElementHandle
    and ensure that it exists.

    Args:
        element: The Playwright ElementHandle to wait within.
        query: The CSS selector string of the element to wait for.

    Raises:
        Exception: If no element is found after waiting (i.e., result is None).

    Returns:
        The ElementHandle object matching the selector once it appears.
    """
    result = await element.wait_for_selector(query)

    if result is None:
        raise Exception(f"Error: waited for '{query}', received None.")

    return result