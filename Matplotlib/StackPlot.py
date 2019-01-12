# working with stack plot

from matplotlib import pyplot

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
studying = [2,3,4,4,3]
playing = [7,8,7,2,2]
eating = [8,5,7,8,13]

pyplot.plot([ ],[ ],label = "Sleeping",color = 'r',linewidth = '5')
pyplot.plot([ ],[ ],label = "Studying",color = 'm',linewidth = '5')
pyplot.plot([ ],[ ],label = "Playing",color = 'c',linewidth = '5')
pyplot.plot([ ],[ ],label = "Eating",color = 'k',linewidth = '5')

pyplot.stackplot(days ,sleeping,studying,playing,eating,color = ['r','m','c','k'])

pyplot.title("My Daily Schedule")
pyplot.xlabel("X-axis")
pyplot.ylabel("Y-axis")
pyplot.legend()
pyplot.show()