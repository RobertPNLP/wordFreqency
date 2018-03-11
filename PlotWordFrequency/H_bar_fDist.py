
import matplotlib.pyplot as plt
import numpy as np
from gettingStartedWordFDist import topTenSortedFDist as topTenFDist
import numpy

userInput = input('What summary would you like to look up?  ')
topTen = topTenFDist(userInput)


plt.rcdefaults()
fig, ax = plt.subplots()

x_data = list()
y_data = list()

for i in range(0,len(topTen)):
    y_data.append(topTen[i][1])
    x_data.append(topTen[i][0])
print(x_data)

    
x_data = numpy.array(x_data)
y_data = numpy.array(y_data).astype(np.int)


y_tick = numpy.std(y_data, axis=0)
y_tick = np.round(y_tick,0)
y_tickList = list()
maxY = np.amax(y_data)

for i in range(0,len(x_data)):
    temp = y_tick*i
    temp = np.round(temp,0)
    if(temp<maxY):
        y_tickList.append(temp)
    else:
        temp = y_tick*(i)
        temp = np.round(temp,0)
        y_tickList.append(temp)
        break
print(y_tickList)
ax.barh(x_data, y_data, align='center', color='green')
ax.set_xticks(y_tickList)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Word Frequency')
ax.set_title('Top Ten Most Commom Words in Wiki Summary: ' + userInput.capitalize())

plt.show()
