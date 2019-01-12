# TextBook example page no:- 157

from matplotlib import pyplot

alcholicContent = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
percentage = [43.75,49.76,53.25,51.23,53.57,65.75,70.33,74.24,75.62,75.63,79.98,81.25,100]

pyplot.bar(alcholicContent,percentage,color = 'purple')

pyplot.xlabel("Year")
pyplot.ylabel("Percentage")
pyplot.legend()
pyplot.title('After Watching "Bharat Anu Nenu" Education System in India')

pyplot.show()
