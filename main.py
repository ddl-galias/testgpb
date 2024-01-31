import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import sys
minx = float(sys.argv[1])
maxx = float(sys.argv[2])
tick = int(sys.argv[3])
x = np.linspace(minx, maxx, tick)
y = np.sin(x)
plt.plot(x, y, 'o', color='black')
plt.savefig("/mnt/artifacts/plot.png")