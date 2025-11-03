import re
from playwright.async_api import ElementHandle, Page
from classes import MenuItem, MenuOptionCategory, MenuOptionChoice
from utility import query_selector, query_selector_all, wait_for_selector

async def scrape_modal(element: ElementHandle, page: Page) -> MenuItem:
    """
    Scrape a menu item from a modal dialog on the page, including its name,
    price, and option categories with choices.

    Args:
        element: The ElementHandle representing the clickable element that opens the modal.
        page: The Playwright Page object to interact with.

    Returns:
        A MenuItem object containing the scraped information.
    """
    await element.click()

    item = MenuItem()

    name = await wait_for_selector(page, "*[role='dialog'] h1")
    name_value = await name.text_content()

    price = await wait_for_selector(page, "*[role='dialog'] *[data-testid='menu-item-price'] > *")
    price_text = await price.text_content()
    price_text = price_text[1:]  # remove '$'
    price_value = 0.0
    try:
        price_value = float(price_text)
    except ValueError:
        pass

    option_categories = await query_selector_all(page, "*[role='dialog'] ul li > div[data-testid]", 0)

    for option_category in option_categories:
        category = MenuOptionCategory()

        option_category_name_container = await query_selector(option_category, "div:first-child > div:first-of-type > div:first-of-type")
        divs = await query_selector_all(option_category_name_container, "*")
        option_category_name_div = divs[0]
        option_category_name = await option_category_name_div.text_content()

        if len(divs) > 1:
            other_div = divs[1]
            span = await other_div.query_selector("span")
            if span is None:
                category.amount_limit = 1  # default if no text
            else:
                text = await span.text_content()
                amount = int(re.findall(r'\d+', text)[0])
                category.amount_limit = amount
                if "up to" not in text:
                    category.amount_required = amount

        option_choices = await query_selector_all(option_category, "div:last-child div[data-testid]")
        for option_choice in option_choices:
            choice = MenuOptionChoice()
            name_elem = await query_selector(option_choice, "div > div > div > div:first-child")
            choice.name = await name_elem.text_content()

            price_elem = await option_choice.query_selector("div > div > div > div:nth-child(3)")
            choice.price = 0.0
            if price_elem is not None:
                price_text = await price_elem.text_content()
                price_text = price_text[2:]  # remove '+$'
                choice.price = float(price_text)

            category.choices.append(choice)

        category.name = option_category_name
        item.options_categories.append(category)

    close_button = await query_selector(page, "*[data-baseweb='modal'] *[data-baseweb='button'][aria-label='Close']")
    await close_button.click()

    item.name = name_value
    item.price = price_value
    return item