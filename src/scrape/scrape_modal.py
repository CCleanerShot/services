import re
from playwright.async_api import ElementHandle, Page
from classes import MenuItem, MenuOptionCategory, MenuOptionChoice
from utility import query_selector, query_selector_all, wait_for_selector


async def scrape_modal(element: ElementHandle, page: Page) -> MenuItem:
    await element.click()

    item = MenuItem()
    name = await wait_for_selector(page, "*[role='dialog'] h1")
    name_value = await name.text_content()
    price = await wait_for_selector(page, "*[role='dialog'] *[data-testid='menu-item-price'] > *")
    price_text = await price.text_content()
    price_text = price_text[1:] # remove '$'
    price_value = 0.0

    try:
        price_value = float(price_text)
    except:
        pass
        
    option_categories = await query_selector_all(page, "*[role='dialog'] ul li > div[data-testid]", 0)

    for option_category in option_categories:
        category = MenuOptionCategory()

        option_categories_names = await query_selector(option_category, "div:first-child > div:first-of-type > div:first-of-type")
        divs = await query_selector_all(option_categories_names, "*")
        option_category_name_div = divs[0]
        option_category_name = await option_category_name_div.text_content()

        if divs.__len__() > 1:
            other_div = divs[1]
            span = await other_div.query_selector("span")

            if span == None:
                category.amount_limit = 1 # assuming because there's no text
            else:
                # TODO: dont simply extract for the number later
                text = await span.text_content()
                amount = re.findall(r'\d+\.?\d*', text)[0]
                category.amount_limit = amount

                if text.find("up to") == -1:
                    category.amount_required = amount

        option_choices = await query_selector_all(option_category, "div:last-child div[data-testid]")
        
        for option_choice in option_choices:
            choice = MenuOptionChoice()
            name = await query_selector(option_choice, "div > div > div > div:first-child")
            name_value = await name.text_content()

            price = await option_choice.query_selector("div > div > div > div:nth-child(3)")
            price_value = 0.0

            if price != None:
                price_text = await price.text_content()
                price_text = price_text[2:] # remove '+$'
                price_value = float(price_text)
            
            choice.name = name_value
            choice.price = price_value
            category.choices.append(choice)

        category.name = option_category_name
        item.options_categories.append(category)
    
    close_button = await query_selector(page, "*[data-baseweb='modal'] *[data-baseweb='button'][aria-label='Close']")
    await close_button.click()

    item.name = name_value
    item.price = price_value
    return item