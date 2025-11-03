import sys
from anthropic import Anthropic


def determine_orders(query: str, restaurant: str, history: object, context: object):
    client = Anthropic()

    system_prompt = """
    Based on the query and restaurant, determine what the user wants to order. Use the user's history and restaurant's context to aid in determining the order.

    When giving a response 
    """

    client.messages.create(messages=[query], system=system_prompt, )


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if args.__len__() != 2:
            raise Exception("Usage: determine_orders.py <query> <history> <context>")

        query = args[0]

        result = determine_orders(query)
    
    except Exception as e:
        print(f"Error: {e}")