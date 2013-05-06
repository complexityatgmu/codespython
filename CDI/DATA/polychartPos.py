'''
Created on Apr 29, 2013

@author: josemagallanes
'''
from xlrd import open_workbook
import pylab


maxY=0
maxX=0
data2 = open_workbook('polydata.xls')
coords = data2.sheet_by_index(0)
coordList=[]
for rownum in range(1,coords.nrows):
    coordList.append(coords.row_values(rownum))

for i in range(len(coordList)):
    if maxY< coordList[i][2]:maxY= coordList[i][2]
    if maxX< coordList[i][1]:maxX= coordList[i][1]
    pylab.text(coordList[i][1],coordList[i][2],coordList[i][0])
    pylab.plot(coordList[i][1],coordList[i][2], 'bo', c='r')

pylab.ylim([0,10*int((maxY/10)+1)])
pylab.xlim([0,10*int((maxX/10)+1)])    
pylab.grid(color='g', linestyle='--', linewidth=0.5)
pylab.show()