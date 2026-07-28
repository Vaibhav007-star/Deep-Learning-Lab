 – Step-by-Step Explanation

This document explains every part of the Perceptron Learning Algorithm used to implement an **AND Gate**.

---

# Step 1: Import NumPy


import numpy as np


### Explanation

- `NumPy` is a Python library used for numerical and mathematical operations.
- It allows us to work efficiently with arrays and perform vector calculations.
- In this program, NumPy is mainly used for:
  - Creating arrays
  - Performing the dot product
  - Initializing weights


# Step 2: Define the Input Data


X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])


### Explanation

This is the training dataset.

Each row represents one training example.

| Sample | Input |
|--------|--------|
| 1 | [0,0] |
| 2 | [0,1] |
| 3 | [1,0] |
| 4 | [1,1] |

There are:

- 4 training samples
- 2 input features

These are all possible combinations of an AND gate.


# Step 3: Define the Expected Output


y = np.array([0,0,0,1])


### Explanation

This array stores the correct outputs for each input.

| Input | Expected Output |
|--------|-----------------|
| [0,0] | 0 |
| [0,1] | 0 |
| [1,0] | 0 |
| [1,1] | 1 |

The perceptron learns by comparing its prediction with these expected outputs.


# Step 4: Initialize the Weights


weights = np.zeros(2)

### Explanation

Since there are **2 input features**, the perceptron requires **2 weights**.

Initially,


weights = [0,0]

where

w1 = 0
w2 = 0

Weights determine how important each input feature is during prediction.



# Step 5: Initialize the Bias


bias = 0

### Explanation

The bias is an additional parameter that shifts the decision boundary.

The perceptron calculates


Output = (w1 × x1) + (w2 × x2) + bias

Without a bias, the decision boundary would always pass through the origin.



# Step 6: Set the Learning Rate


learning_rate = 0.1

### Explanation

The learning rate determines **how much the weights and bias change after each mistake**.

- Small learning rate → Slow learning
- Large learning rate → Faster learning (may become unstable)

In this project,

Learning Rate = 0.1




# Step 7: Set the Number of Epochs

epochs = 10


### Explanation

An **epoch** means one complete pass through the entire training dataset.

Since there are four training samples,


1 Epoch = 4 Training Examples


The model repeats this process 10 times to gradually improve its predictions.



# Step 8: Start Training


for epoch in range(epochs):


### Explanation

This loop repeats the complete training process for 10 epochs.

Inside it,


for i in range(len(X)):


processes every training sample one by one.



# Step 9: Calculate the Weighted Sum


summation = np.dot(X[i], weights) + bias


### Explanation

The perceptron first calculates a weighted sum.

Mathematically,


Summation = (x1 × w1) + (x2 × w2) + bias


Example:

Suppose


Input = [1,1]

Weights = [0.3,0.2]

Bias = -0.1


Then
Summation

= (1 × 0.3)

+ (1 × 0.2)

- 0.1

= 0.4


# Understanding np.dot()


np.dot(X[i], weights)

### Explanation

`np.dot()` calculates the **dot product** between the input vector and the weight vector.

Example 1

Input

[1,0]

Weights

[0.2,0.5]


Calculation

(1 × 0.2)

+

(0 × 0.5)

=

0.2


Example 2


Input

[1,1]

Weights

[0.2,0.5]


Calculation


(1 × 0.2)

+

(1 × 0.5)

=

0.7


The dot product combines the inputs and weights into a single value before adding the bias.


# Step 10: Apply the Activation Function

prediction = 1 if summation >= 0 else 0

### Explanation

The perceptron uses the **Step Activation Function**.

Rule

If Summation ≥ 0

↓

Prediction = 1

Otherwise

↓

Prediction = 0

This converts the weighted sum into a binary output (0 or 1).


# Step 11: Calculate the Error


error = y[i] - prediction

### Explanation

The error tells us whether the prediction was correct.

Formula

**
Error = Actual Output - Predicted Output**

Examples

Correct output is 1

Prediction is 0

```
Error = 1
```

Correct output is 0

Prediction is 1

```
Error = -1
```

Correct output is 1

Prediction is 1

```
Error = 0
```

If the error is zero, the perceptron made the correct prediction.

---

# Step 12: Update the Weights

```python
weights += learning_rate * error * X[i]
```

### Explanation

The perceptron adjusts its weights whenever it makes a mistake.

Formula

```
New Weight

=

Old Weight

+

Learning Rate

×

Error

×

Input
```

Example

```
Old Weights

[0,0]

Input

[1,1]

Learning Rate

0.1

Error

1
```

Weight Update

```
0.1 × 1 × [1,1]

=

[0.1,0.1]
```

New Weights

```
[0.1,0.1]
```

This allows the perceptron to learn from its mistakes.

---

# Step 13: Update the Bias

```python
bias += learning_rate * error
```

### Explanation

The bias is updated in the same way.

Formula

```
New Bias

=

Old Bias

+

Learning Rate

×

Error
```

Example

```
Old Bias = 0

Error = 1

Learning Rate = 0.1

New Bias

= 0 + 0.1

= 0.1
```

Updating the bias shifts the decision boundary to improve future predictions.

---

# Step 14: Testing the Model

```python
for i in range(len(X)):
```

### Explanation

After training is complete, the perceptron uses the **final learned weights and bias** to predict the outputs for all input combinations.

The training process is finished, and no more weight updates occur during testing.

---

# First Epoch Example

### Initial Values

```
Weights = [0,0]

Bias = 0
```

---

### Input = [0,0]

Expected Output

```
0
```

Weighted Sum

```
0
```

Prediction

```
1
```

Error

```
0 - 1 = -1
```

Updated Values

```
Weights = [0,0]

Bias = -0.1
```

---

### Input = [0,1]

Weighted Sum

```
-0.1
```

Prediction

```
0
```

Error

```
0
```

No update.

---

### Input = [1,0]

Weighted Sum

```
-0.1
```

Prediction

```
0
```

Error

```
0
```

No update.

---

### Input = [1,1]

Weighted Sum


-0.1


Prediction

0

Expected Output

1


Error
1


Updated Values

Weights = [0.1,0.1]

Bias = 0

After several epochs, the perceptron correctly learns the AND gate.


# Perceptron Learning Flow

Training Data
      │
      ▼
Initialize Weights & Bias
      │
      ▼
For Each Epoch
      │
      ▼
Read One Training Sample
      │
      ▼
Calculate Weighted Sum
      │
      ▼
Apply Step Activation Function
      │
      ▼
Predict Output
      │
      ▼
Compare with Expected Output
      │
      ▼
Calculate Error
      │
      ▼
Update Weights & Bias
      │
      ▼
Repeat Until Training Ends
      │
      ▼
Test the Model
      │
      ▼
Predict AND Gate Outputs

- Training Process
- Prediction Process
- AND Gate Classification
