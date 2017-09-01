import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)
x_values = list(range(1, 1000))
y_values = [x**2 for x in range(1, 1000)]
plt.scatter(x_values, y_values, s=1, edgecolors='none',
            c=y_values, cmap=plt.cm.Blues)

plt.title("Square Number", fontsize=25)
plt.xlabel("Value", fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()
