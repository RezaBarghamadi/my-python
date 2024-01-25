import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.colors import LogNorm 
dx, dy = 0.016, 0.06
P = np.arange(-5.0, 5.0, dx) 
print(P, "\n"*3) 
Q = np.arange(-5.0, 5.0, dy) 
print(Q, "\n"*3) 
P, Q = np.meshgrid(P, Q) 
print(P, "\n"*3, Q) 
  
min_max = np.min(P), np.max(P), np.min(Q), np.max(Q) 
res = np.add.outer(range(8), range(8)) % 2
plt.imshow(res, cmap="binary_r") 
plt.xticks([]) 
plt.yticks([]) 
plt.title("Using Matplotlib Python to Create chessboard") 
plt.show() 