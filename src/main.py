import asyncio
import sys

from determine_intent import determine_intent
from determine_restaurant import determine_restaurant


async def main(query: str, userID: str, latitude: float, longitude: float) -> bool:
    intent = determine_intent(query)

    if intent == "Order":
        # query restaurants who are close in promixity to the user
        restaurant = determine_restaurant(query, )
    else:
        # get the question
        pass
    
    return True


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if args.__len__() != 4:
            raise Exception("Usage: main.py <query> <userID> <latitude> <longitude>")

        query, userID, latitude, longitude = args[0], args[1], args[2], args[3]
        result = asyncio.run(main(query, userID, latitude, longitude))
        print(result)
    except Exception as e:
        print(f"Error: {e}")