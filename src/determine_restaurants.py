import sys
from anthropic import Anthropic


def determine_restaurant(query: str, history: object):
    client = Anthropic()

    system_prompt = """
    Based on the order, combined with the user's purchase history, respond with only the name of the restaurant they are likely referring to. If you cannot determine the restaurant, respond with 'N/A'.
    """

    result = f"""
    User History:
    
    """

    client.messages.create(messages=[query], system=system_prompt)


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if args.__len__() != 1:
            raise Exception("Usage: determine_restaurant.py <query> <history>")

        query = args[0]

        result = determine_restaurant(query)
    
    except Exception as e:
        print(f"Error: {e}")