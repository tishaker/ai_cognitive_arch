import numpy as np

# A simple conversational mind that stays open and remembers your words
vocabulary = {}

print("==================================================")
print("Interactive Mind Initialized. It is waiting for you.")
print("==================================================")

while True:
    # This input() function forces the program to pause and wait for you
    user_input = input("\nYou: ").lower().strip()
    
    if user_input == "exit":
        print("Goodbye!")
        break
        
    if user_input not in vocabulary:
        print("AI: I don't understand that word yet.")
        meaning = input("-> Teach the AI what this word means (e.g., happy, scary): ")
        vocabulary[user_input] = meaning
        print(f"[Success: Learned that '{user_input}' means '{meaning}']")
    else:
        current_feeling = vocabulary[user_input]
        print(f"AI: *Recognizes word* -> Current State: [{current_feeling.upper()}]")
