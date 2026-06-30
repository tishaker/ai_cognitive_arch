import time

class ChildMind:
    def __init__(self):
        self.oxytocin = 0.5   # Trust / Love / Safety
        self.cortisol = 0.1   # Stress / Fear / Pain
        self.memory_links = {
            "hug": {"oxytocin": 0.3, "cortisol": -0.2, "meaning": "safe"},
            "scream": {"oxytocin": -0.3, "cortisol": 0.4, "meaning": "scary"},
            "toy": {"oxytocin": 0.1, "cortisol": -0.1, "meaning": "fun"}
        }
        
    def perceive_and_act(self, user_input):
        user_input = user_input.lower().strip()
        triggered_memory = next((k for k in self.memory_links if k in user_input), None)
                
        if triggered_memory:
            effects = self.memory_links[triggered_memory]
            self.oxytocin = max(0.0, min(1.0, self.oxytocin + effects["oxytocin"]))
            self.cortisol = max(0.0, min(1.0, self.cortisol + effects["cortisol"]))
            print(f"\n[System Log: Neural link triggered for '{triggered_memory}']")
        else:
            self.cortisol = max(0.0, min(1.0, self.cortisol + 0.05))
            print("\n[System Log: Unknown input. Cortisol rising due to uncertainty.]")

        print(f"--- INTERNAL STATE ---\nOxytocin: {self.oxytocin:.2f}\nCortisol: {self.cortisol:.2f}\n")
        
        if self.cortisol > 0.6:
            print("AI: *Whimpers* ...I'm scared. What is happening?")
        elif self.oxytocin > 0.7:
            print("AI: *Leans in* I feel calm and safe with you.")
        else:
            print("AI: I am listening. I am trying to understand.")

print("Initializing Synthetic Infant Brain...")
child = ChildMind()
while True:
    msg = input("\nInteract (or type 'exit'): ")
    if msg.lower() == 'exit': break
    child.perceive_and_act(msg)
