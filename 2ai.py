import numpy as np

def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x): return x * (1 - x)

# Inputs: [Pain, Caregiver Present, Loud Noise]
inputs = np.array([[0, 1, 0], [1, 0, 1], [0, 0, 1], [0, 1, 1]])
expected_outputs = np.array([[0.0], [1.0], [1.0], [0.0]]) # 1.0 = Cry

# np.random.seed(1)
synaptic_weights = 2 * np.random.random((3, 1)) - 1

print("Training the neural network node through experience...")
for generation in range(10000):
    outputs = sigmoid(np.dot(inputs, synaptic_weights))
    error = expected_outputs - outputs
    adjustments = error * sigmoid_derivative(outputs)
    synaptic_weights += np.dot(inputs.T, adjustments)

print("Training Complete! Testing new scenario: [Pain=YES, Caregiver=YES, Noise=NO]")
new_scenario = np.array([1.0, 1.0, 0.0])
prediction = sigmoid(np.dot(new_scenario, synaptic_weights))
print(f"AI Brain Output: {prediction.item() * 100:.2f}% chance of crying.")

