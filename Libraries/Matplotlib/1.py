import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]     # X-axis values
y = [2, 4, 6, 8, 10]    # Y-axis values

plt.plot(x, y)          # Creates a line plot (connects points with a line)
plt.title("Simple Line Plot")  # Adds a title
plt.xlabel("X Axis")           # Labels the X-axis
plt.ylabel("Y Axis")           # Labels the Y-axis
plt.show()                     # Displays the graph

fruits = ['Apple', 'Mango', 'Banana']
sales = [ 7, 6, 12]
plt.bar(fruits, sales)
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.title('Sales of Fruits')
plt.show()

ages = [15, 18, 21, 21, 24, 30]

plt.hist(ages, bins=5, color='darkblue', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age Ranges")
plt.ylabel("Count")
plt.show()

x = [5,7,8,7,6,9,5,6,7,8]
y = [99,86,87,88,100,86,103,87,94,78]

plt.scatter(x, y)
plt.title("Scatter Example")
plt.show()

x = [1,2,3,4,5]
y1 = [1,4,9,16,25]   # Squares
y2 = [1,2,3,4,5]     # Linear

plt.plot(x,y1, label="Squares")
plt.plot(x,y2, label="Linear")
plt.legend()
plt.show()

x = [1, 2, 3, 4, 5]     # X-axis values
y = [2, 4, 6, 8, 10]    # Y-axis values
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.title("Styled Line")
plt.grid(True)
plt.show()
plt.savefig("mygraph.png")

