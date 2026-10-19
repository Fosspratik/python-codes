import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Parameters
n = 10
p = 0.5

# Possible number of successes: 0 to 10
x = np.arange(0, n + 1)

# Calculate binomial probabilities
binom_probs = stats.binom.pmf(x, n, p)

# Plot
plt.bar(x, binom_probs, width=0.6,
        color="skyblue", edgecolor="black")

plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of successes")
plt.ylabel("Probability")
plt.xticks(x)
plt.show()
