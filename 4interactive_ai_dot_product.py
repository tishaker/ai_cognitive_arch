import numpy as np

# 1. The Intelligent Dictionary (The Neural Embedding Space)
# Each word is mapped to a 2D coordinate matrix: [Joy Score, Fear Score]
vocabulary = {
    "hello": np.array([0.5, 0.0]),
    "hug":   np.array([0.9, -0.4]),
    "scary": np.array([-0.3, 0.8]),
    "stop":  np.array([-0.2, 0.9]),
    "friend":np.array([0.8, -0.2])
}

# The child's internal baseline emotional state
internal_oxytocin = 0.5  # Trust/Calmness

print("==================================================")
print("Vector-Based Interactive Mind Active. Talk to it.")
print("==================================================")

while True:
    user_input = input("\nYou: ").lower().strip()
    
    if user_input == "exit":
        print("Goodbye!")
        break
        
    # Split the sentence into individual words
    words = user_input.split()
    sentence_vector = np.array([0.0, 0.0])
    words_found = 0
    
    # 2. Math Processing: Summing the vectors of your sentence
    for word in words:
        if word in vocabulary:
            sentence_vector += vocabulary[word]
            words_found += 1
            
    # 3. The Cognitive Step
      # 3. Cognitive Processing & Learning Layer
    if words_found > 0:
        sentence_vector /= words_found
        joy, fear = sentence_vector[0], sentence_vector[1]
        
        internal_oxytocin += (joy - fear) * 0.2
        internal_oxytocin = max(0.0, min(1.0, internal_oxytocin))
        
        print(f"[System Math Log -> Calculated Input Impact: Joy={joy:.2f}, Fear={fear:.2f}]")
        print(f"[Internal State  -> Current Oxytocin (Trust Level): {internal_oxytocin:.2f}]")
        
        if internal_oxytocin < 0.3:
            print("AI: *Recoils* ...I feel unsafe. Please speak kindly.")
        elif internal_oxytocin > 0.7:
            print("AI: *Smiles* I feel incredibly safe with you right now.")
        else:
            print("AI: I hear you. I am processing your words.")
    else:
        # Dynamic Learning Loop: If it doesn't know the words, it asks for the coordinates!
        print("AI: *Tilts head* I don't know those words yet.")
        new_word = input("-> Which single word from your sentence should I learn? ").lower().strip()
        try:
            user_joy = float(input(f"-> Enter Joy value for '{new_word}' (-1.0 to 1.0): "))
            user_fear = float(input(f"-> Enter Fear value for '{new_word}' (-1.0 to 1.0): "))
            
            # Save the new word into the NumPy vocabulary array
            vocabulary[new_word] = np.array([user_joy, user_fear])
            print(f"[Success: Trained neural coordinate for '{new_word}' -> Joy={user_joy}, Fear={user_fear}]")
        except ValueError:
            print("[System Error: Please enter valid numbers next time!]")
        
        # 4. Behavioral Output Layer
        if internal_oxytocin < 0.3:
            print("AI: *Recoils* ...I feel unsafe. Please speak kindly.")
        elif internal_oxytocin > 0.7:
            print("AI: *Smiles* I feel incredibly safe with you right now.")
        else:
            print("AI: I hear you. I am processing your words.")