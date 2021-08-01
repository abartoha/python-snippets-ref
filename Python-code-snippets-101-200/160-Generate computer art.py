'''
Python Code Snippets vol #32
https://stevepython.wordpress.com/full-python-code-snippets-list/

160-Generate computer art

pip3 install numpy
pip3 install matplotlib

Source:
https://dev.to/codesharedot/computer-generated-art-with-python-3ala
'''

import numpy as np
import matplotlib.pyplot as plt


N = 100
x = np.zeros(N)
y = np.zeros(N)

for i in range(N):
    x[i] = np.random.rand()
    y[i] = np.random.rand()
colors = np.random.rand(N)

area = (30 * np.random.rand(N))**2
ax = plt.subplot(111)
ax.scatter(x, y, s=area, c=colors, alpha=0.6)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.axis('off')
plt.show()
