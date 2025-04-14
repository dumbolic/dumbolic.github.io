import requests
import json
import random
import pyttsx3  # For local TTS (if you're not using a cloud service)
import os

# Initialize pyttsx3 TTS engine
engine = pyttsx3.init()

# Function to get random quote
def get_quote():
    try:
        r = requests.get("https://zenquotes.io/api/random")
        return r.json()[0]['q'] + " – " + r.json()[0]['a']
    except:
        return "Stay positive, work hard, make it happen."

# Function to get random fact
def get_fact():
    try:
        r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        return r.json()["text"]
    except:
        return "Octopuses have three hearts."

# Function to get crypto prices
def get_crypto():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd")
        prices = r.json()
        return {
            "BTC": f"${prices['bitcoin']['usd']:,}",
            "ETH": f"${prices['ethereum']['usd']:,}"
        }
    except:
        return {"BTC": "$65,000", "ETH": "$3,200"}

# Function to get random tip
def get_tip():
    tips = [
        "Comment your code – Future You will thank you.",
        "Use version control, even for small projects.",
        "Don't repeat yourself (DRY principle).",
        "Use `alt` tags for images to improve accessibility."
    ]
    return random.choice(tips)

# Function to get the latest news (placeholder for now)
def get_news():
    return "NASA's Artemis mission preps for lunar base in 2035."  # placeholder

# Function to get a random joke
def get_joke():
    try:
        r = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        return r.json()["joke"]
    except:
        return "Why do programmers prefer dark mode? Because light attracts bugs."

# Function to get the word of the day
def get_word_of_the_day():
    # This can be made dynamic with an API later
    return {
        "word": "ephemeral",
        "definition": "Lasting for a very short time."
    }

# Function to convert text to speech (TTS)
def text_to_speech(text, filename="audio_output.mp3"):
    try:
        # Ensure the 'audio' directory exists
        os.makedirs("audio", exist_ok=True)
        audio_file = f"audio/{filename}"
        engine.save_to_file(text, audio_file)
        engine.runAndWait()
        return audio_file
    except Exception as e:
        print(f"Error in text-to-speech conversion: {e}")
        return None

# Generate content.json
content = {
    "quote": get_quote(),
    "fact": get_fact(),
    "book": "Sapiens: A Brief History of Humankind – Yuval Noah Harari",
    "tip": get_tip(),
    "crypto": get_crypto(),
    "song": "Bohemian Rhapsody – Queen",
    "news": get_news(),
    "joke": get_joke(),
    "word_of_the_day": get_word_of_the_day()
}

# Save content data to JSON file
with open("content.json", "w") as f:
    json.dump(content, f, indent=2)

# Generate real-time audio from quote and fact
quote_audio = text_to_speech(content['quote'], "quote_audio.mp3")
fact_audio = text_to_speech(content['fact'], "fact_audio.mp3")

# Print out the audio file paths generated
if quote_audio:
    print(f"Quote audio saved as: {quote_audio}")
if fact_audio:
    print(f"Fact audio saved as: {fact_audio}")
