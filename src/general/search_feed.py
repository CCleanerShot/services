import asyncio
from playwright.async_api import Page
from constants import DELAY_PAGE_LOAD, DELAY_SEARCH_BOX
from utility import error_search_url, query_selector_all, wait_for_selector

async def search_feed(page: Page, restaurant: str):
    search_input = await wait_for_selector(page, "input[type='text']")
    await search_input.fill(restaurant)
    await asyncio.sleep(DELAY_SEARCH_BOX)

    ul = await wait_for_selector(page, "ul[role='listbox']")
    lis = await query_selector_all(ul, "*")
    li = lis[0]
    await li.click()
    await asyncio.sleep(DELAY_PAGE_LOAD)

    url = page.url

    if(url.find("/store") == -1):
        raise Exception(error_search_url(search_feed, "/store", url))