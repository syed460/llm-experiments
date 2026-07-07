import json
from pathlib import Path

PRICES = json.loads(
    Path(__file__).with_name("prices.json").read_text(encoding="utf-8")
)

tools = [{
    "type": "function",                                     
    "function": {
        "name": "get_price",                                
        "description": "Get the price of a shop item the user asks about.", 
        "parameters": {                                      
            "type": "object",
            "properties": {
                    "item": { "type": "string", "description": "the item name"}
                },
            "required": [
                "item"
                ],
        },
    },
}]


def get_price(item) -> dict:
    print(f"🔧 tool called: get_price({item})")
    # return {
    #         "item": item,
    #         "price": PRICES.get(item.lower(), 'unknown'),
    #         "currency": "INR"
    #     }
    price = PRICES.get(item.lower(), 'unknown')
    return f"₹{price}"