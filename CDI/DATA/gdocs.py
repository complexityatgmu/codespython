'''
Created on Mar 23, 2013
@author: JoseManuel MAGALLANES
For NSF - CDI Project
Center for Social Complexity - George Mason University
ONLY FOR INTERNAL USE
'''
import gspread
import matplotlib.pyplot as plot
from scipy import stats
from math import log

'''OUR PRIVATE parameters'''
username = 'datacsc.gmu@gmail.com'
password = 'krasnowgmu'
filename = 'fema-declarations'

dataFromCloud = gspread.login(username,password)
dataToManipulate = dataFromCloud.open(filename).sheet1 #sheet1 if the data is in the FIRST sheet in the spreadsheet
words=[x for x in dataToManipulate.col_values(1)[1:]] #not considering name of field
uniques = set(words)
freqs = [words.count(item) for item in uniques]
data=sorted(freqs, reverse=True)
rankdata=sorted(stats.rankdata(data))

#HISTOGRAM
plot.figure(1)
plot.hist(data, normed=True)
plot.title('HISTOGRAM')   
plot.xlabel('Number of Disaster Declarations in a US State')
plot.ylabel('p(x)')
plot.text(200,20,"Kurtosis= %f" %stats.kurtosis(data),fontsize=12,fontweight='bold')
plot.text(200,21,"Skewness= %f" %stats.skew(data),fontsize=12,fontweight='bold')
plot.savefig('histogram.png')

#CUMMULATIVE
plot.figure(2)
plot.hist(data,normed=True,cumulative=True)
plot.title('Cummulative distribution')   
plot.xlabel('Number of Disaster Declarations in a US State')
plot.ylabel('P(X<x)')
plot.savefig('cumm.png')

#SCATTERPLOT
plot.figure(3)
plot.scatter([rankdata[i] for i in range(len(rankdata))],[data[i] for i in range(len(data))], color='b') 
plot.title('SCATTERPLOT')   
plot.xlabel('Rank of Disaster Declarations in a US State')
plot.ylabel('Number of Disaster Declarations in a US State')
plot.savefig('scatter.png')

#LOG-LOG 
plot.figure(4)
plot.scatter([log(rankdata[i]) for i in range(len(rankdata))],[log(data[i]) for i in range(len(data))], color='b')
plot.title('LOG-LOG')   
plot.xlabel('LOG(Rank of Disaster Declarations in a US State)')
plot.ylabel('LOG(Number of Disaster Declarations in a US State')
plot.savefig('loglogscatter.png')


'''OPTIONAL: remove '#' to uncomment next lines if you want a copy for excel. 
YOU will get a CSV with the same name of GoogleDoc file'''
#import os
#import csv
#allData = dataToManipulate.get_all_values()
#takeHome=csv.writer(file(os.path.join(filename + '.csv'),'wb'),dialect='excel')
#takeHome.writerows(allData)
