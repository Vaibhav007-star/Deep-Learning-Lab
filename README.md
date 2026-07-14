# Deep Learning Lab 1 - Perceptron using NumPy

A simple implementation of the **Perceptron Algorithm** in Python using **NumPy**. This program demonstrates binary classification by simulating the **AND Logic Gate**.

---

## 📌 Objective

To implement a simple Perceptron model using NumPy and train it to classify the outputs of an AND gate.

---

## 🛠️ Technologies Used

- Python 3.x
- NumPy
- Visual Studio Code

---

## 📂 Project Structure

```
Deep-Learning-Lab/
│── Lab-1.py
│── README.md
└── .gitignore
```

---

## 🚀 Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Deep-Learning-Lab.git
```

### 2. Open the Project

```bash
cd Deep-Learning-Lab
```

### 3. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Command Prompt**

```cmd
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install numpy
```

### 6. Run the Program

```bash
python Lab-1.py
```

---

## 📖 Program Description

The program performs the following steps:

1. Imports the NumPy library.
2. Creates the input dataset for the AND gate.
3. Initializes weights and bias.
4. Trains the perceptron using the learning rule.
5. Updates weights and bias based on prediction errors.
6. Displays the final weights, bias, and predictions.

---

## 📊 Input Dataset

| Input 1 | Input 2 | Expected Output |
|---------:|---------:|----------------:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

---

## ✅ Expected Output

```
Final Weights: [0.2 0.1]
Final Bias: -0.2

Predictions:
Input: [0 0] -> Output: 0
Input: [0 1] -> Output: 0
Input: [1 0] -> Output: 0
Input: [1 1] -> Output: 1
```

> *The learned weights may vary slightly depending on the training process, but the predictions should remain the same.*

---

## 📚 Concepts Covered

- Perceptron
- Binary Classification
- Step Activation Function
- Weight Update Rule
- Supervised Learning
- NumPy

---

## 👨‍💻 Author

**Vaibhav**

Deep Learning Laboratory – College Practical

---
