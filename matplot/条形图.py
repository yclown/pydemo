import matplotlib.pyplot as plt

import numpy as np
#https://www.jb51.net/article/105287.htm
y = [20, 10, 30, 25, 15]

index = np.arange(5)

plt.bar(left=index, height=y, color='green', width=0.5)

plt.show()