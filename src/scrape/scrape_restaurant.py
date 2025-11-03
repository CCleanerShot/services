# TODO: future, diff from the base average restaurant's items, instead of unique ones for each location
from classes import MenuItem
from scrape import scrape_modal
from utility import query_selector_all
from general import search_feed, search_home
from playwright.async_api import async_playwright

async def scrape_restaurant(restaurant: str, location: str) -> list[MenuItem]:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.ubereats.com", timeout=45000)

        await search_home(page, location)
        await search_feed(page, restaurant)
        items = await query_selector_all(page, "*[data-testid='store-catalog-section-vertical-grid'] li")
        
        results = []
        for item in items:
            result = await scrape_modal(item, page)
            results.append(result)

        return results