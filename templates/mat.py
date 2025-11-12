import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [2, 4, 9, 16, 25]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y, color='blue')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Line Plot between x and y')

plt.subplot(1, 2, 2)
plt.scatter(x, y, color='red')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Scatter Plot between x and y')

plt.show()
