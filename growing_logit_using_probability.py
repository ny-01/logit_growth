import numpy as np
import matplotlib.pyplot as plt

# Original probabilities p
p = np.linspace(0.001, 0.999, 500)  # avoid exact 0 or 1

# Different logit step sizes to visualize
x_values = [0.1, 0.5, 1, 2, 3]

plt.figure(figsize=(8,5))

for x in x_values:
    # Compute probability increase l for each p
    l = (np.exp(x)-1) * p * (1-p) / (1 - p + p * np.exp(x))
    plt.plot(p, l, label=f'logit increase x={x}')

# Add the derivative curve: instantaneous rate of change of p w.r.t logit
derivative = 1 / (p * (1 - p))  # dz/dp
# Clip derivative for plotting to avoid huge spikes near 0 and 1
derivative = np.clip(derivative, 0, 20)

plt.plot(p, derivative, '--', color='black', label='Derivative 1/(p(1-p))')

plt.xlabel('Original probability p')
plt.ylabel('Increase in probability l')
plt.title('Change in probability for various logit increases\nwith local derivative')
plt.grid(True)
plt.legend()
plt.show()