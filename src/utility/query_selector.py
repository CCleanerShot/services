from playwright.async_api import ElementHandle


async def query_selector(element: ElementHandle, query: str):
    result = await element.query_selector(query)

    if result == None:
        raise Exception(f"Error: searched {query}, received None.")

    return result