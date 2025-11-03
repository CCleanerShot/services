import asyncio
import sys
from general import search_feed, search_home
from playwright.async_api import async_playwright


evaluate = """
() => { const entries = [
    [
        "eatsPassSelectedPersonalPayment",
        "null"
    ],
    [
        "eats:membership_preview_hero_xp_parameter_value",
        "true"
    ],
    [
        "eats:store_breadcrumb_impression-c4f9f903-e786-4fe3-8c62-f902805c252a",
        "true"
    ],
    [
        "trackingCode",
        "{'metaInfo':{'pluginName':'NationalFavoritesIGPlugin','analyticsLabel':'national_favorites','verticalType':'UNKNOWN','category':'','subcategory':'','surfaceAreaV2':'HOME_FEED','additionalTrackingData':{'predictionUUID':'55fb05c7-b7e3-4083-9e0b-68d613895e84','tracingID':'3010d514-c7a8-446c-8bee-ef4c36ea04eb'}},'storePayload':{'storeUUID':'c4f9f903-e786-4fe3-8c62-f902805c252a','isOrderable':true,'score':{'breakdown':{'ConversionRatePredictionScore':0.01677853614091873,'ConversionRateScoreCoefficient':1.72,'FinalScore':0.026274230844084565,'HmooScorePreSCR':0.03274492774158716,'NetInflowPredictionScore':21.830528259277344,'NetInflowScoreCoefficient':0,'PredictionScore':0.03274492774158716,'ServiceQualityPredictionScore':0.95,'ServiceQualityScoreCoefficient':0,'StoreCarouselRelevanceFactor':1,'StoreCarouselRelevanceScore':0.8023908634470861,'beta_coefficient_scaling_factor':0,'conversion_rate_boosting_factor':1.72,'conversion_rate_partial_score':0.01677853614091873,'ctr_boosting_factor':1.72,'ctr_partial_score':0.0022592125460505486,'lw_conversion_rate_boosting_factor':1.72,'lw_conversion_rate_partial_score':0.0022592125460505486,'model_signature--esr-v7-t1-retrain-no-bool-fp32-mig':1,'net_inflow_boosting_factor':0,'net_inflow_partial_score':21.830528259277344,'service_quality_boosting_factor':0,'service_quality_partial_score':0.95,'t120d_eyeball_count':2848},'total':0.026274230844084565},'etdInfo':{'dropoffETASec':849,'dropoffETARange':{'min':10,'max':10,'raw':10},'minRangeDropoffETASec':600,'maxRangeDropoffETASec':600,'etdMode':'PREDICTION'},'ratingInfo':{'storeRatingScore':4.614042738770176,'ratingCount':'5,000+'},'scheduleTimeSlots':null,'isDBF':true,'storeAvailablityState':'NOT_ACCEPTING_ORDERS'}}"
    ],
    [
        "u_scsid_r",
        "nXR0mhzEBddiaT3YW0STWpkHMBxjiIQWFjygmUo3wXiU7dXggYOXO-cUaY8sy43630nN0aIMduvT5ovigSsdvp-Z3odvikwKpHtHZMyHBa8qcllm"
    ],
    [
        "_cid_cc_ck",
        "ARq0Jt/ZlL9Lz6v+dOnAm/df"
    ],
    [
        "tt_appInfo",
        "{'platform':'pc'}"
    ],
    [
        "store_session:c4f9f903-e786-4fe3-8c62-f902805c252a",
        "5c39052b-2d92-423e-b9a2-b01c46b76fff"
    ],
    [
        "hasVisitedFeed",
        "true"
    ],
    [
        "xlb_page_loaded_beacon_fired",
        "true"
    ],
    [
        "store.pcb.existing_cart_last_surfaced_store",
        "c4f9f903-e786-4fe3-8c62-f902805c252a"
    ],
    [
        "u_scsid",
        "lPR0mhzEBddiaT3YW0STWpkHMBxjiIQWSTfBeJTt1eCBg5c75xRpjyzLjfrfSc3Rogx26tLmi-KBKx2-n5neh2-KTAqke0dkzIcFrypyWWU"
    ],
    [
        "uev2.lvs",
        "c4f9f903-e786-4fe3-8c62-f902805c252a"
    ],
    [
        "eats:eats_web_cro_store_dish_rating_inclusion",
        "true"
    ],
    [
        "eatsPassPaymentProfiles",
        "[]"
    ],
    [
        "eats:membership_preview_hero_xp_inclusion_event",
        "true"
    ],
    [
        "_cc_ck",
        "ARq0Jt/ZlL9Lz6v+dOnAm/df"
    ],
    [
        "tt_sessionId",
        "'2f52852a-b8d1-11f0-8621-ea396e1c69bf::V0KD9mYhAlomLvzZwY3Z'"
    ],
    [
        "tt_pixel_is_enrich_ipv6_triggered_by_enrich_am",
        "true"
    ],
    [
        "tt_pixel_session_index",
        "{'index':3,'main':1}"
    ]
];

for (const [k, v] of entries) {
    window.sessionStorage.setItem(k, v)
}
}
"""

async def add_order(order: str) -> bool:
    pass


async def order_food(address: str, restaurant: str, orders: list[str]) -> bool:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await browser.new_page()
        await page.goto("https://www.ubereats.com", timeout=45000)
        await page.evaluate(evaluate)
        await search_home(page, address)
        await search_feed(page, restaurant)
        state = await context.storage_state(path="sessions.json")

        "2f52852a-b8d1-11f0-8621-ea396e1c69bf::V0KD9mYhAlomLvzZwY3Z"
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