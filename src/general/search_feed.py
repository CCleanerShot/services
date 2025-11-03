import asyncio
from playwright.async_api import Page
from constants import DELAY_PAGE_LOAD, DELAY_SEARCH_BOX
from utility import error_search_url, query_selector_all, wait_for_selector

async def search_feed(page: Page, restaurant: str):
    """
    Search for a restaurant in a search box on the page, select the first result,
    and verify that the resulting page URL contains '/store'.

    Args:
        page: The Playwright Page object to interact with.
        restaurant: The name of the restaurant to search for.

    Raises:
        Exception: If the resulting page URL does not contain '/store'.
    """
    search_input = await wait_for_selector(page, "input[type='text']")
    await search_input.fill(restaurant)
    await asyncio.sleep(DELAY_SEARCH_BOX)

    ul = await wait_for_selector(page, "ul[role='listbox']")
    lis = await query_selector_all(ul, "*")
    li = lis[0]

    await li.click()
    await asyncio.sleep(DELAY_PAGE_LOAD)

    url = page.url

    if "/store" not in url:
        raise Exception(error_search_url(search_feed, "/store", url))