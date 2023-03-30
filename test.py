import numpy as np
import matplotlib.pyplot as plt


arr = np.array([])
mu = 0
sigma = 10

for i in range(0, 50): 
    while True:
        number = np.random.normal(mu, sigma)
        if -50 <= number <= 50:
            arr = np.append(arr, number)
            break


plt.hist(arr, bins=50)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')

plt.show()

