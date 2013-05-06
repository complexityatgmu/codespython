import matplotlib.pyplot as plot
from xlrd import open_workbook
import networkx as nx
from itertools import combinations
import math
import os
print os.getcwd()
#os.chdir('/Users/josemagallanes/Documents/workspace/PHDMASON/CDI/data')
#
#print os.getcwd()

data1 = open_workbook("polyNet.xls")
dyads = data1.sheet_by_index(0)
listNeighbors=[]
for dyad in range(dyads.nrows):
    listNeighbors.append(dyads.cell_value(dyad,0)) #second column has the ids

data2 = open_workbook('polydata.xls')
coords = data2.sheet_by_index(0)
coordList=[]

for rownum in range(1,coords.nrows):
    coordList.append(coords.row_values(rownum))

polychart=nx.Graph()
pos={}
for country in coordList:    
    pos.update ({country[0]:(country[1],country[2])})
polychart.add_nodes_from(pos.keys())

for i in range(len(listNeighbors)):
    edges = combinations(listNeighbors[i].split(", "), 2)
    for edge in edges:
        node1,node2=edge
        polychart.add_edge(node1, node2)


nodeDegreeCent=nx.degree(polychart)
nodeDegreeClos=nx.closeness_centrality(polychart)
nodeDegreeBetw=nx.betweenness_centrality(polychart)

print [float(nodeDegreeCent[x]) for x in polychart]
print [nodeDegreeClos[x] for x in polychart]
print [nodeDegreeBetw[x] for x in polychart]
#nodecolor=[float(polychart.degree(v)) for v in polychart]
degree= [float(math.pow(5+nodeDegreeCent[x],3)) for x in polychart]
#nodecolor= [nodeDegreeClos[x] for x in polychart]
betweeness=[nodeDegreeBetw[x] for x in polychart]
nx.draw(polychart, pos, node_size=degree,node_color=betweeness, alpha=0.8, linewidths=0, cmap='RdYlGn')#cmap=plot.cm.Reds_r)
plot.colorbar()
plot.xlim(0, 78)
plot.ylim(0, 100)
plot.show()

#for n, p in pos.iteritems():
#    polychart.node[n]['pos'] = p
#nx.draw(polychart, pos, node_color='w', alpha=0.8, linewidths=0)
