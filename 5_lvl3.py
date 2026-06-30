import torch
import torch.nn as nn
import torch.optim as optim
import os
import random

actions = ["*stares blankly*", "*cries*", "*coos*", "*recoils*", "hello?", "friend?"]
num_actions = len(actions)

class GrowingMind(nn.Module):
    def __init__(self):
        super(GrowingMind, self).__init__()
        self.network = nn.Sequential(nn.Linear(3, 16), nn.ReLU(), nn.Linear(16, num_actions))
    def forward(self, x): return self.network(x)

brain = GrowingMind()
optimizer = optim.Adam(brain.parameters(), lr=0.1)
criterion = nn.MSELoss()
SAVE_PATH = "child_identity.pt"

if os.path.exists(SAVE_PATH):
    brain.load_state_dict(torch.load(SAVE_PATH))
    print("[Loaded previous day's memories.]")

day = 1
while True:
    user_in = input(f"\n[Day {day}] You: ").lower().strip()
    if user_in == "exit":
        torch.save(brain.state_dict(), SAVE_PATH)
        break

    tone = 1.0 if any(w in user_in for w in ["good", "love", "hug", "hello"]) else -1.0
    sensory_input = torch.tensor([1.0, tone, float(len(user_in))])

        # 30% chance to explore a new behavior, 70% chance to use learned memory
    if random.random() < 0.30:
        chosen_idx = random.randint(0, num_actions - 1)
        print("[System Log: Child is exploring a random new reaction...]")
    else:
        with torch.no_grad():
            probs = brain(sensory_input)
            chosen_idx = torch.argmax(probs).item()

    
    print(f"Child: {actions[chosen_idx]}")
    feedback = input("\nType '1' for Reward, '-1' for Correction: ")
    
    if feedback in ['1', '-1']:
        targets = probs.clone()
        targets[chosen_idx] += float(feedback)
        optimizer.zero_grad()
        loss = criterion(brain(sensory_input), targets)
        loss.backward()
        optimizer.step()
    day += 1
