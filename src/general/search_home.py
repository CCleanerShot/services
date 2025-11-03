import asyncio
from playwright.async_api import Page

from constants import DELAY_PAGE_LOAD, DELAY_SEARCH_FILL
from utility import error_search_url, wait_for_selector

async def search_home(page: Page, location: str):
    """
    Fill the home page search input with a location, click the continue button,
    and verify that the resulting page URL contains '/feed'.

    Args:
        page: The Playwright Page object to interact with.
        location: The location string to search for.

    Raises:
        Exception: If the resulting page URL does not contain '/feed'.
    """
    search_input = await wait_for_selector(page, "input[type='text']")
    continue_button = await wait_for_selector(page, "button[data-testid='find-food-button']")

    await search_input.fill(location)
    await asyncio.sleep(DELAY_SEARCH_FILL)
    await continue_button.click()

    await asyncio.sleep(DELAY_PAGE_LOAD)

    url = page.url
    
    if "/feed" not in url:
        raise Exception(error_search_url(search_home, "/feed", url))