# main.py

# Introduction
print("👋 Hey there! I’m CryptoBuddy — your AI-powered sidekick for smart crypto decisions! Let’s get growing 🌱🚀")
print("⚠️ Disclaimer: Crypto investing is risky. This bot provides guidance, not financial advice. Always DYOR!\n")

# Crypto dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# Function for recommendation logic
def get_recommendation(query):
    query = query.lower()

    if "sustainable" in query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 {best} is the most sustainable! Low energy use and strong long-term potential."

    elif "trending" in query or "rising" in query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 Trending cryptos right now: {', '.join(trending)}."

    elif "long-term" in query or "growth" in query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                return f"🚀 {name} looks promising for long-term growth — rising trend and strong sustainability!"
        return "🤔 No strong long-term options found right now."

    elif "energy" in query:
        low_energy = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
        return f"🔋 These cryptos use the least energy: {', '.join(low_energy)}."

    else:
        return "🤖 Hmm, I’m not sure. Try asking about sustainability, trends, or growth."

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("CryptoBuddy: Goodbye! 🌍 Remember — always do your own research! 📚")
        break
    response = get_recommendation(user_input)
    print(f"CryptoBuddy: {response}\n")
