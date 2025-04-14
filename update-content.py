import requests, json, random
import os  # To access environment variables

# Get the Weather API key and News API key from environment variables
weather_api_key = os.getenv('WEATHER_API')
news_api_key = os.getenv('NEWS_API_KEY')

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
    if not news_api_key:
        print("Error: News API key not found!")
        return [
            {"title": "AI is revolutionizing healthcare", "link": "https://example.com/ai-health"},
            {"title": "Quantum computing breakthroughs announced", "link": "https://example.com/quantum"}
        ]
    try:
        response = requests.get(
            f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={news_api_key}"
        )
        articles = response.json().get("articles", [])
        tech_news = [{"title": article["title"], "link": article["url"]} for article in articles]
        return tech_news
    except Exception as e:
        print(f"Error fetching tech news: {e}")
        return [
            {"title": "AI is revolutionizing healthcare", "link": "https://example.com/ai-health"},
            {"title": "Quantum computing breakthroughs announced", "link": "https://example.com/quantum"}
        ]

def get_sports_news():
    if not news_api_key:
        print("Error: News API key not found!")
        return [
            {"title": "India defeats Australia in last-over thriller", "link": "https://example.com/cricket"},
            {"title": "Real Madrid advances to UCL final", "link": "https://example.com/football"}
        ]
    try:
        response = requests.get(
            f"https://newsapi.org/v2/top-headlines?category=sports&apiKey={news_api_key}"
        )
        articles = response.json().get("articles", [])
        sports_news = [{"title": article["title"], "link": article["url"]} for article in articles]
        return sports_news
    except Exception as e:
        print(f"Error fetching sports news: {e}")
        return [
            {"title": "India defeats Australia in last-over thriller", "link": "https://example.com/cricket"},
            {"title": "Real Madrid advances to UCL final", "link": "https://example.com/football"}
        ]

def get_weather():
    if not weather_api_key:
        print("Error: Weather API key not found!")
        return {
            "location": "Unknown",
            "temp": "N/A",
            "description": "N/A"
        }
    try:
        r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q=Mumbai")
        r.raise_for_status()  # Check if the request was successful
        data = r.json()
        return {
            "location": data["location"]["name"],
            "temp": data["current"]["temp_c"],
            "description": data["current"]["condition"]["text"]
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
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
