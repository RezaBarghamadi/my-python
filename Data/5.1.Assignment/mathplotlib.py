import numpy as np
import matplotlib.pyplot as plt

height= np.array([80, 85, 90, 95, 100, 120])
weghit = np.array([150, 160, 175, 180, 185, 190,])

plt.title("Test Plot")
plt.xlabel("weghit 😎")
plt.ylabel("height 🙂")

plt.plot(height, weghit)

plt.grid()

plt.show()