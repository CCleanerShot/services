import sys
from anthropic import Anthropic


def determine_intent(query: str):
    client = Anthropic()

    system_prompt = """
    Determine if the message is a question or an order. Do not immediately assume it's a question if it has a question mark. If removing the question mark would make it an order, classify it as an order. Only ever answer with "Order" or "Question". If you are unsure, default to question. You will be given the user's order history to get more context.
    """

    client.messages.create(messages=[query], system=system_prompt)


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if args.__len__() != 1:
            raise Exception("Usage: determine_intent.py <query>")

        query = args[0]

        result = determine_intent(query)
    
    except Exception as e:
        print(f"Error: {e}")