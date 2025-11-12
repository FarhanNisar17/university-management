import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5,6,]
y = [i**2 for i in x]
z = [i**3 for i in x]

plt.plot(x, x, label='x')
plt.plot(x, y, label='x²')
plt.plot(x, z, label='x³')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('x, x² and x³ in one plot')
plt.legend()
plt.show()
