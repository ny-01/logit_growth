# Logistic Regression Probability Increment Visualizer

This tool visualizes how changes in the log-odds (logit) translate into changes in the predicted probability \(p\) in logistic regression.

## Features

- Plots the increase in probability \(l\) required to achieve different fixed increases in logit \(x\), for a range of starting probabilities \(p\).
- Includes the derivative curve \(p(1-p)\), which represents the instantaneous rate of change of probability with respect to logit.
- Allows intuitive comparison between finite logit increments and local linear approximations.

## Usage

- Run the provided Python script or notebook.
- Modify the list `x_values` to explore different logit step sizes.
- Observe how the increment \(l\) varies with \(p\) for each \(x\), and how the derivative curve forms a natural bound for small \(x\).

## Requirements

- Python 3.x
- `numpy`
- `matplotlib`

Install dependencies with:

```bash
pip install numpy matplotlib
```

## Insights

- The derivative curve \(p(1-p)\) peaks at \(p = 0.5\), indicating maximum sensitivity of probability to logit changes.

- For small \(x\), the probability increment \(l\) approaches the derivative curve, confirming the local linear approximation.

- For larger \(x\), the curves demonstrate the logistic function’s nonlinear “squashing” behavior, especially near \(p = 0\) and \(p = 1\).