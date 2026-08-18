# Irrigation Decision Perceptron

A simple, real-life example of a **single-layer perceptron** that automates an irrigation ON/OFF decision for a crop field.

## Problem Statement

A farmer wants a basic automated system to decide whether to turn irrigation **ON** or **OFF**, based on two sensor readings:

| Feature | Meaning |
|---|---|
| Soil Dry? | `1` = soil is dry, `0` = soil is moist |
| No Rain Expected? | `1` = no rain forecast, `0` = rain expected |

**Rule:** Irrigate only when the soil is dry **AND** no rain is expected. Otherwise, watering is unnecessary or wasteful.

This is logically an **AND gate**, which a perceptron can learn perfectly since it's linearly separable.

## Truth Table

| Soil Dry | No Rain Expected | Decision |
|---|---|---|
| 0 | 0 | OFF |
| 0 | 1 | OFF |
| 1 | 0 | OFF |
| 1 | 1 | **ON** |

## How It Works

1. **Inputs (`X`)** — 4 combinations of the two binary sensor readings.
2. **Labels (`y`)** — the correct irrigation decision for each combination.
3. **Weights & Bias** — start at zero, and are updated during training.
4. **Activation Function** — a step function: output is `1` if the weighted sum ≥ 0, else `0`.
5. **Training Loop** — runs for 10 epochs. For each sample:
   - Compute the prediction.
   - Compare it to the expected output to get the `error`.
   - Adjust `weights` and `bias` proportionally to the error and learning rate.
6. **Testing** — after training, the model predicts irrigation decisions for all 4 input combinations and prints them with human-readable labels.

## Files

| File | Description |
|---|---|
| `Lab-1.py` | Python script implementation |
| `Lab-1.ipynb` | Jupyter/Colab notebook version |
| `README.md` | This file |

## Requirements

- Python 3.x
- NumPy

```bash
pip install numpy
```

## Run It

```bash
python Lab-1.py
```

or open `Lab-1.ipynb` in Jupyter Notebook / Google Colab and run all cells.

## Sample Output
