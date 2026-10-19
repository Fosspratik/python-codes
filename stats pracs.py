import matplotlib.pyplot as plt
import numpy as np
import scipy
# Parameters
x = np.arange(0, n+1) # possible number of successes
# Calculate binomial probabilities
binom_probs = stats.binom.pmf(x, n, p)
# Plot
plt.bar(x, binom_probs, width=0.6, color="skyblue")
edgecolor="black"
plt.title('Binomial Distribution (n=10, p=0.5)')
plt.xlabel('Number of successes&#39')
plt.ylabel('Probability')
plt.show()
