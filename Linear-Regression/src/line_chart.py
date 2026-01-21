#create a line chart using matplotlib
import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
# Create a line chart
plt.plot(x, y, marker='o')
# Add title and labels  
plt.title('Sample Line Chart')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
# Show the chart
plt.show()
