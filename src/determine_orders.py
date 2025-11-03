import sys
import dotenv
from anthropic import Anthropic

dotenv.load_dotenv()

def determine_orders(query: str, restaurant: str, history: object, restaurant_items_context: object):
    client = Anthropic()

    system_prompt = """
    Based on the query and restaurant, determine what the user wants to order. Use the user's history and restaurant's context to aid in determining the order. If there is no history, ignore the history.

    When giving a response 

    If you cannot determine what the user is ordering, simply respond with 'N/A'.
    """

    client.messages.create(messages=[query], system=system_prompt)


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if args.__len__() != 3:
            raise Exception("Usage: determine_orders.py <query> <history> <restaurant_items_context>")

        query, history, restaurant_items_context = args[0], args[1], args[2]
        result = determine_orders(query, history, restaurant_items_context)
        print(result)
    

    except Exception as e:
        print(f"Error: {e}")