import requests
import json

def get_quote():
    try:
        r = requests.get("https://zenquotes.io/api/random")
        return r.json()[0]['q'] + " – " + r.json()[0]['a']
    except:
        return "Stay positive, work hard, make it happen."

def get_fact():
    try:
        r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        return r.json()["text"]
    except:
        return "Octopuses have three hearts."

def get_crypto():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd")
        prices = r.json()
        return f"BTC: ${prices['bitcoin']['usd']}, ETH: ${prices['ethereum']['usd']}"
    except:
        return "BTC: $65,000, ETH: $3,200"

def get_tip():
    tips = [
        "Comment your code – Future You will thank you.",
        "Use version control, even for small projects.",
        "Don't repeat yourself (DRY principle).",
        "Use `alt` tags for images to improve accessibility."
    ]
    return tips[0]

def get_news():
    return "NASA's Artemis mission preps for lunar base in 2035."  # Use real API later

# Generate content.json
content = {
    "quote": get_quote(),
    "fact": get_fact(),
    "book": "Sapiens: A Brief History of Humankind – Yuval Noah Harari",
    "tip": get_tip(),
    "crypto": get_crypto(),
    "song": "Bohemian Rhapsody – Queen",
    "news": get_news()
}

with open("content.json", "w") as f:
    json.dump(content, f, indent=2)
