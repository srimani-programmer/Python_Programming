
from matplotlib import pyplot

time = [12,34,36,13,5]
work = ['Eating','Playing','Studying','Sleeping','chatting']
col = ['r','g','b','purple','yellow']

pyplot.pie(time,labels = work,colors= col,startangle=90,shadow=False,explode=(0,0,0,0,0),autopct= '%0.1f%%' )

pyplot.title("Holidays Schedule")
pyplot.show()