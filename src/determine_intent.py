import sys
import dotenv
from typing import get_args
from anthropic import Anthropic
from literals import MessageType

dotenv.load_dotenv()

def determine_intent(query: str) -> MessageType:
    client = Anthropic(api_key="")

    system_prompt = """
    Determine if the message is a question or an order. Do not immediately assume it's a question if it has a question mark. If removing the question mark would make it an order, classify it as an order. Only ever answer with "Order" or "Question". If you are unsure, default to question.
    """

    response = client.messages.create(messages=[{"role": "user", "content": query}], system=system_prompt, max_tokens=1024, model="claude-sonnet-4-5-20250929")
    text = str(response.content[0].text)
    
    if text not in get_args(MessageType):
        raise Exception(f"Expected {get_args(MessageType)}, received {text}. You should attempt it again, or adjust the prompt...")
    
    return text


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        if args.__len__() != 1:
            raise Exception("Usage: determine_intent.py <query>")

        query = args[0]
        result = determine_intent(query)
        print(result)
    
    except Exception as e:
        print(f"Error: {e}")