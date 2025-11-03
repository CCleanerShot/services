import asyncio
from playwright.async_api import Page

from constants import DELAY_PAGE_LOAD, DELAY_SEARCH_FILL
from utility import error_search_url, wait_for_selector

async def search_home(page: Page, location: str):
    search_input = await wait_for_selector(page, "input[type='text']")
    continue_button = await wait_for_selector(page, "button[data-testid='find-food-button']")
    await search_input.fill(location)
    await asyncio.sleep(DELAY_SEARCH_FILL)
    await continue_button.click()

    await asyncio.sleep(DELAY_PAGE_LOAD)

    url = page.url

    if(url.find("/feed") == -1):
        raise Exception(error_search_url(search_home, "/feed", url))