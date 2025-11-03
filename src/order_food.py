import asyncio
import sys
from general import search_feed, search_home
from playwright.async_api import async_playwright


async def add_order(order: str) -> bool:
    pass


async def order_food(address: str, restaurant: str, orders: list[str]) -> bool:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.ubereats.com", timeout=45000)
        await search_home(page, address)
        await search_feed(page, restaurant)
    return True

if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if args.__len__() != 3:
            raise Exception("Usage: order_food.py <address> <restaurant> <orders>")

        address, restaurant, orders = args[0], args[1], args[2]
        result = asyncio.run(order_food(address, restaurant, orders))
    
    except Exception as e:
        print(f"Error: {e}")