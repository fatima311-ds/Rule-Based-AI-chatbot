from datetime import datetime

# ================= Welcome Screen =================

print("=" * 52)
print("            🤖 Welcome to Nexora AI")
print("      Your Intelligent Rule-Based Assistant")
print()
print("✨ Explore intelligent conversations.")
print("🚀 Discover smart features built with Python.")
print("-" * 52)
print("Available Commands:")
print("✔ hello   → Greeting")
print("✔ hi      → Greeting")
print("✔ help    → Show all commands")
print("✔ time    → Current Time")
print("✔ date    → Today's Date")
print("✔ what's your name → Bot Name")
print("✔ thanks  → Appreciation")
print("✔ bye     → End Conversation")
print("✔ exit    → Close Nexora AI")
print()
print('Type "help" anytime to see this menu again.')
print("=" * 52)

# ================= Dictionary =================

responses = {
    "hello": "Hello! 👋 Welcome. How can I help you today?",
    "hi": "Hello! 👋 Welcome. How can I help you today?",
    "what's your name": "My name is Nexora AI. 🤖",
    "what is your name": "My name is Nexora AI. 🤖",
    "your name": "My name is Nexora AI. 🤖",
    "thanks": "You're most welcome! I'm always happy to help 😊",
    "bye": "👋 Goodbye! Have a wonderful day!"
}

# ================= Chatbot =================

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "help":
        print("\n📋 Available Commands:")
        print("👋 hello")
        print("👋 hi")
        print("🕑 time")
        print("📅 date")
        print("🤖 what's your name")
        print("🙏 thanks")
        print("👋 bye")
        print("❌ exit")

    elif user_input == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Nexora AI: Today's 🕑 time is {current_time}.")

    elif user_input == "date":
        today_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Nexora AI: Today's 📅 date is {today_date}.")

    elif user_input == "exit":
        print("👋 Nexora AI is shutting down...")
        break

    else:
        response = responses.get(user_input)

        if response:
            print(f"Nexora AI: {response}")

            if user_input == "bye":
                break
        else:
            print("Nexora AI: ❌ Sorry, I didn't understand that command.")
            print("💡 Type 'help' to see available commands.")