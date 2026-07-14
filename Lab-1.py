import numpy as np

# Input data (AND Gate)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output
y = np.array([0, 0, 0, 1])

# Initialize weights and bias
weights = np.zeros(2)
bias = 0
learning_rate = 0.1
epochs = 10

# Training
for epoch in range(epochs):
    for i in range(len(X)):
        summation = np.dot(X[i], weights) + bias

        # Activation function
        prediction = 1 if summation >= 0 else 0

        # Update weights and bias
        error = y[i] - prediction
        weights += learning_rate * error * X[i]
        bias += learning_rate * error

# Testing
print("Final Weights:", weights)
print("Final Bias:", bias)

print("\nPredictions:")
for i in range(len(X)):
    summation = np.dot(X[i], weights) + bias
    prediction = 1 if summation >= 0 else 0
    print(f"Input: {X[i]} -> Output: {prediction}")