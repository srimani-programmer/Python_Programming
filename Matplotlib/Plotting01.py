# Drawing a general graph

from matplotlib import pyplot

x = [-5,-1,0,4,7,12,15,17,19,27]
y = [-11,-9,0,6,14,19,23,27,31,35]

pyplot.plot(x,y,color = 'r',label = 'General Plotting')

pyplot.legend()
pyplot.xlabel("X-axis")
pyplot.ylabel("Y-axis")
pyplot.show()