from playwright.async_api import ElementHandle


async def query_selector_all(element: ElementHandle, query: str, required_length = 1):
    result = await element.query_selector_all(query)

    if result.__len__() < required_length:
        raise Exception(f"Error: expected atleast 1 element from {query}, received 0.")

    return result
