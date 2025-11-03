import sys
import dotenv
from anthropic import Anthropic

dotenv.load_dotenv()

def determine_restaurant(query: str, surrounding_restaurants_context: str):
    client = Anthropic()

    system_prompt = """
    Based on the order, combined with the user's purchase history, respond with only the name of the restaurant they are likely referring to. You will be given a list of existing restaurants near the user as well. If you cannot determine the restaurant, respond with 'N/A'.
    """

    result = f"""
    User History:
    
    """

    client.messages.create(messages=[query], system=system_prompt)


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if args.__len__() != 2:
            raise Exception("Usage: determine_restaurant.py <query> <surrounding_restaurants_context>")

        query, surrounding_restaurants_context = args[0], args[1]
        result = determine_restaurant(query, surrounding_restaurants_context)
    
    except Exception as e:
        print(f"Error: {e}")