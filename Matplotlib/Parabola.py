# Drawing a parabola

from matplotlib import pyplot
from matplotlib import style

style.use('ggplot') # This is used to apply the style sheet of the graph
x_axisvalues = [0,1,3,5,6]
y_axisvalues = [5,0,-4,0,5]
x1_axisvalues = [5,2]
y1_axisvalues =[0,-2]

pyplot.plot(x_axisvalues,y_axisvalues,'r',label ="parabola",linewidth = 1.7)
pyplot.plot(x1_axisvalues,y1_axisvalues,'g',label = 'line',linewidth = 2.0)

pyplot.title("Parabola")
pyplot.ylabel("Y-axis")
pyplot.xlabel("x-axis")
pyplot.grid(True,color = 'b')   # This function is link with layout of the graph
pyplot.legend() # This function is link with label

pyplot.show()   # this function is used to display the content