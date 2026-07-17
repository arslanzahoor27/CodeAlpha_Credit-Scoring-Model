def start_chatbot():
    # 1. KNOWLEDGE BASE (Intent Architecture)
    # A. Responses: Yahan hum sirf bot ke final jawabaat rakhenge, har jawab ka ek ID (intent) hoga.
    responses = {
        "greeting": "Hello! I am your AI assistant. How can I help you?",
        "pricing": "Our basic plan starts at $10/month.",
        "status": "I am functioning perfectly, thank you!"
    }
    
    # B. Intent Map: Yahan hum user ke mukhtalif words ko ek hi Intent ke sath link karenge.
    intent_map = {
        "hello": "greeting",
        "hi": "greeting",
        "hey": "greeting",
        "salam": "greeting",
        "price": "pricing",
        "cost": "pricing",
        "charges": "pricing",
        "how are you": "status"
    }
    
    fallback_message = "I'm sorry, I don't understand that command. Can you rephrase?"

    print("System Initialized. Type 'exit' to quit.")

    # 2. INPUT LOOP
    while True:
        raw_input = input("You: ")
        
        # 3. SANITIZATION (Data Clean Karna)
        clean_input = raw_input.lower().strip().replace("?", "")
        
        # 4. EXIT STRATEGY
        if clean_input in ['exit', 'bye', 'quit']:
            print("Bot: Goodbye! Have a great day.")
            break
        
        # 5. LOOKUP & FALLBACK (Two-Step Verification)
        # Step A: User ke word se Intent dhoondo
        detected_intent = intent_map.get(clean_input)
        
        # Step B: Us Intent ka actual response dhoondo. Agar intent na mile, to fallback do.
        bot_response = responses.get(detected_intent, fallback_message)
        
        # 6. OUTPUT
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    start_chatbot()