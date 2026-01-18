# Matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Matplotlib Basics

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a simple line graph
plt.plot(x, y)

# Add title and labels
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Subplots

# Accessing first subplot
plt.subplot(2,2,1)

# plotting 
plt.subplot(2,2,1)
plt.plot(x, np.sin(x))
plt.title("Sine Wave")
plt.subplot(2,2,2)
plt.plot(x, np.cos(x))
plt.title("Cosine Wave")
plt.subplot(2,2,3)
plt.plot(x, np.tan(x))
plt.title("Tangent Wave")
plt.subplot(2,2,4)
plt.plot(x, np.exp(-x))
plt.title("Exponential Decay")

# Object-Oriented Approach
# Figsize creates a figure with specified width and height
# DPI sets the resolution of the figure
fig = plt.figure(figsize=(8,6) , dpi=100)
fig

# adding axes
axis1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # [left, bottom, width, height]
axis1.plot(x, y)

# adding second axes
axis2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
axis2.plot(x, np.cos(x))

# Type of plots

# Scatter Plot
plt.scatter(x, y)

# Histogram
data = np.random.randn(1000)
plt.hist(data)

# Box Plot
plt.boxplot(data)

# Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]
plt.bar(categories, values)

# Saving Plots
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x, y)
# save the plot as a PNG file
plt.savefig("plot.png")

# Working with Images
# Importing image module
import matplotlib.image as mpimg

img = mpimg.imread('1.avif')

# Displaying the image
plt.imshow(img)
# it is optional to hide the axes
plt.axis('off')

# Cropping can be done using array slicing if needed
cropped_img = img[50:200, 100:300]
plt.imshow(cropped_img)
plt.axis('off')

# Designing Plots
xaxis = np.linspace(0,5,11)

fig, ax = plt.subplots(figsize=(12,6))

ax.plot(xaxis, xaxis+1, color="red", linewidth=0.25)
ax.plot(xaxis, xaxis+2, color="red", linewidth=0.50)
ax.plot(xaxis, xaxis+3, color="red", linewidth=1.00)
ax.plot(xaxis, xaxis+4, color="red", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(xaxis, xaxis+5, color="green", lw=3, linestyle='-')
ax.plot(xaxis, xaxis+6, color="green", lw=3, ls='-.')
ax.plot(xaxis, xaxis+7, color="green", lw=3, ls=':')

# custom dash
line, = ax.plot(xaxis, xaxis+8, color="black", lw=1.50)
line.set_dashes([5, 50, 15, 50]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(xaxis, xaxis+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(xaxis, xaxis+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(xaxis, xaxis+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(xaxis, xaxis+12, color="blue", lw=3, ls='--', marker='1')
ax.plot(xaxis, xaxis+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(xaxis, xaxis+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(xaxis, xaxis+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(xaxis, xaxis+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");