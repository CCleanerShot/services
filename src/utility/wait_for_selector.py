from playwright.async_api import ElementHandle


async def wait_for_selector(element: ElementHandle, query: str):
    result = await element.wait_for_selector(query)

    if result == None:
        raise Exception(f"Error: waited for {query}, received None.")

    return result