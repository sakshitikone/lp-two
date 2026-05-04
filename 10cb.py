def simple_chatbot():
    print("CoffeeBot: Hello! I'm your virtual assistant. (Type 'quit' to exit)")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ['quit', 'exit', 'bye']:
            print("CoffeeBot: Goodbye! Have a great day.")
            break

        elif any(word in user_input for word in ["hello", "hi", "hey"]):
            print("CoffeeBot: Hi there! How can I help you today?")

        elif any(word in user_input for word in ["hours", "time", "open"]):
            print("CoffeeBot: We are open from 8:00 AM to 8:00 PM every day.")

        elif any(word in user_input for word in ["menu", "coffee", "drink"]):
            print("CoffeeBot: We serve Espresso, Lattes, and Cappuccinos.")

        elif any(word in user_input for word in ["location", "where", "address"]):
            print("CoffeeBot: We are located at 123 Brew Street, downtown.")

        elif any(word in user_input for word in ["price", "cost"]):
            print("CoffeeBot: Prices range from ₹100 to ₹300 depending on your drink.")

        else:
            print("CoffeeBot: I didn’t understand that. Try asking about menu, hours, or location.")


simple_chatbot()

