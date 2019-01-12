# working with histogram

from matplotlib import pyplot

years = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

scientistsValue = [22,52,95,73,253,194,139,127,231,333,457,386,495,599,187,150,659,468,729,121]

pyplot.hist(scientistsValue,years,color='r',label = "Scientist",histtype='bar')

pyplot.title("Analysis of Researching people")
pyplot.xlabel("Year")
pyplot.ylabel('Scientist')
pyplot.legend()

pyplot.show()