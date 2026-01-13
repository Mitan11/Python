# Matplotlib

# This module imports the Matplotlib library for data visualization.
import matplotlib.pyplot as plt

# Sample data for plotting
# X and Y coordinates
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

# Create a simple line plot
plt.plot(x,y)
# Display the plot
plt.show()

# we can specify the marker style using a third argument
# type of marker to use is specified by a character code
# like 'o' for circle, 's' for square, '^' for triangle, etc.
# 'o' specifies circle markers
plt.plot(x,y,'o')
plt.show()

# '*' specifies star markers
plt.plot(x,y,marker='*')
plt.show()

# '*' markers without connecting lines
plt.plot(y,'*')
plt.show()

# we can also specify line style and color
# linestyle can be specified using the 'linestyle' parameter
# line styles can be specified using: - , --,  -.,  : , or using strings like 'solid', 'dashed', 'dashdot', 'dotted'
# '-' for solid line, '--' for dashed line, '-.' for dash-dot line, ':' for dotted line
plt.plot(x,y,'*' , linestyle='-')
plt.show()

plt.plot(x,y,'*' , linestyle=':')
plt.show()

plt.plot(x,y,'*' , linestyle='dotted')
plt.show()

# color can be specified of line using the 'color' parameter
# colors can be specified using single character codes: 'r' for red, 'g' for green, 'b' for blue, 'k' for black, 'c' for cyan, 'm' for magenta, 'y' for yellow, 'w' for white
plt.plot(x,y,'*' , linestyle='dotted' , color = 'r') # r , g, ,b , k , c ,m y , w 
plt.show()

# marker size can be specified using the 'ms' parameter
# default marker size is 6
plt.plot(x,y,'*' , linestyle='dotted' , color = 'r' , ms = 10) # marker size
plt.show()

# marker edge color can be specified using the 'mec' parameter
# default marker edge color is same as marker color
plt.plot(x,y,'*' , linestyle='dotted' , color = 'r' ,ms = 15, mec='c') #mark edge color
plt.show()

# marker face color can be specified using the 'mfc' parameter
# default marker face color is same as marker color
plt.plot(x,y,'*' , linestyle='dotted' , color = 'r' ,ms = 15, mec='c' , mfc='y') #mark face color
plt.show()

# line width can be specified using the 'lw' parameter
# default line width is 1.5
plt.plot(x,y,'*' , linestyle='dotted' , color = 'r' ,ms = 15, mec='c' , mfc='y' , lw=5) # line width
plt.show()

# adding title ,X-axis and Y-axis labels to the plot
plt.plot(x,y,'*' , linestyle='dotted' , color = 'r' ,ms = 15, mec='c' , mfc='y' , lw=5) # line width
# title can be added using the 'title' function
plt.title("Line Chart")
# X-axis label can be added using the 'xlabel' function
plt.xlabel("X-axis")
# Y-axis label can be added using the 'ylabel' function
plt.ylabel("Y-axis")

# we can also customize the font properties of title and labels using the 'fontdict' parameter
# font properties can be specified using a dictionary
font_title = {
    'family' : 'serif', 
    'color' : 'b',
    'size' : 20
}
font_label = {
    'family' : 'serif', 
    'color' : 'g',
    'size' : 15
}
plt.plot(x,y,'*' , linestyle='dotted' , color = 'r' ,ms = 15, mec='c' , mfc='y' , lw=5) # line width
plt.title("Line Chart" , fontdict = font_title)
plt.xlabel("X-axis" , fontdict = font_label)
plt.ylabel("Y-axis" , fontdict = font_label)

# we can also specify the location of the title using the 'loc' parameter
plt.title("Line Chart" , fontdict = font_title , loc = "left") #left , right , center

# Show Multiple Plots in a Single Figure
x1 = [1, 2, 3, 4, 5]
y1 = [10, 15, 13, 17, 20]

x2 = [1, 2, 3, 4, 5]
y2 = [20, 18, 16, 14, 12]

# Method 1: Using multiple plot() calls
plt.plot(x1,y1,'r--', label='Line 1') # red dashed line
plt.plot(x2,y2,'b:', label='Line 2')  # blue dotted line

# Method 2: Using a single plot() call with multiple datasets
plt.plot(x1, y1, x2, y2)

# Adding grid to the plot
plt.plot(x1,y1,x2,y2)
plt.grid()

# using axis parameter to specify which axis to add grid lines to
# parameter values: 'x' , 'y' , 'both'
plt.grid(axis='x') # x,y,both

# specifying color of grid lines using the 'color' parameter
plt.grid(color ='g')

# specifying line style of grid lines using the 'linestyle' parameter
plt.grid(color ='g' , linestyle=':')

# specifying line width of grid lines using the 'linewidth' parameter
plt.grid(color ='g' , linestyle=':' , linewidth=2)

# Subplots : Using subplot() function we can create multiple plots in a single figure
plt.subplot(2,2,1)
plt.plot(x1,y1)
plt.subplot(2,2,2)
plt.plot(x2*2,y2*2)
plt.grid(color ='g' , linestyle=':' , linewidth=2)
plt.subplot(2,2,3)
plt.plot(x2*3,y2*3)
plt.grid(color ='g' , linestyle=':' , linewidth=2)
plt.subplot(2,2,4)
plt.plot(x2*4,y2*4)