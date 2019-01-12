# working with scatter plot

from matplotlib import pyplot

x = [1,2,3,4,5,6,7,8,9]
y = [4,8,3,2,11,9,7,6,3]

x1 = [11,13,15,17,19,23,27]
y1 = [25,29,37,43,56,75,23]

pyplot.scatter(x,y,color = 'r',label = "Analysis1")
pyplot.scatter(x1,y1,color = 'blue',label = "Analysis2")

pyplot.title("Variable Analysis")
pyplot.xlabel("X-axis")
pyplot.ylabel("Y-axis")
pyplot.legend()
pyplot.show()