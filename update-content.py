import requests, json, random

def get_quote():
    try:
        r = requests.get("https://zenquotes.io/api/random")
        return f"{r.json()[0]['q']} – {r.json()[0]['a']}"
    except:
        return "Be yourself; everyone else is already taken. – Oscar Wilde"

def get_fact():
    try:
        r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        return r.json()["text"]
    except:
        return "Honey never spoils."

def get_crypto():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd")
        prices = r.json()
        return f"BTC: ${prices['bitcoin']['usd']:,} | ETH: ${prices['ethereum']['usd']:,}"
    except:
        return "BTC: $0 | ETH: $0"

def get_tip():
    return random.choice([
        "Use keyboard shortcuts to save time.",
        "Commit often with meaningful messages.",
        "Keep your software dependencies updated."
    ])

def get_joke():
    try:
        r = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        return r.json()["joke"]
    except:
        return "Debugging: Being the detective in a crime movie where you are also the murderer."

def get_word():
    return {
        "word": "effervescent",
        "definition": "Vivacious and enthusiastic."
    }

def get_bing_background():
    r = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1")
    img = r.json()['images'][0]['url']
    return f"https://www.bing.com{img}"

def get_youtube_music():
    return "https://www.youtube.com/embed/3JZ4pnNtyxQ?autoplay=1"

def get_tech_news():
    try:
        response = requests.get(
            "https://newsapi.org/v2/top-headlines?category=technology&apiKey=YOUR_API_KEY"
        )
        articles = response.json().get("articles", [])
        tech_news = []
        for article in articles:
            tech_news.append({
                "title": article["title"],
                "link": article["url"]
            })
        return tech_news
    except Exception as e:
        print(f"Error fetching tech news: {e}")
        return [
            {"title": "AI is revolutionizing healthcare", "link": "https://example.com/ai-health"},
            {"title": "Quantum computing breakthroughs announced", "link": "https://example.com/quantum"}
        ]

def get_sports_news():
    try:
        response = requests.get(
            "https://newsapi.org/v2/top-headlines?category=sports&apiKey=2215913e768a49a28d97b55ec0e67ca8"
        )
        articles = response.json().get("articles", [])
        sports_news = []
        for article in articles:
            sports_news.append({
                "title": article["title"],
                "link": article["url"]
            })
        return sports_news
    except Exception as e:
        print(f"Error fetching sports news: {e}")
        return [
            {"title": "India defeats Australia in last-over thriller", "link": "https://example.com/cricket"},
            {"title": "Real Madrid advances to UCL final", "link": "https://example.com/football"}
        ]

def get_weather():
    try:
        key = "demo"  # Replace with real API key
        r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q=Mumbai")
        data = r.json()
        return {
            "location": data["location"]["name"],
            "temp": data["current"]["temp_c"],
            "description": data["current"]["condition"]["text"]
        }
    except:
        return {
            "location": "Unknown",
            "temp": "N/A",
            "description": "N/A"
        }

data = {
    "quote": get_quote(),
    "fact": get_fact(),
    "crypto": get_crypto(),
    "tip": get_tip(),
    "joke": get_joke(),
    "word_of_the_day": get_word(),
    "bing_background": get_bing_background(),
    "youtube_music": get_youtube_music(),
    "tech_news": get_tech_news(),
    "sports_news": get_sports_news(),
    "weather": get_weather()
}

with open("content.json", "w") as f:
    json.dump(data, f, indent=2)
