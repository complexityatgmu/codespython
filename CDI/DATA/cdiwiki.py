'''
Created on Apr 1, 2013

@author: josemagallanes
'''

from xlrd import open_workbook
import urllib2

response = urllib2.urlopen('http://css.gmu.edu/groups/cdiinternal/wiki/87fc9/attachments/c1cd0/DisasterList.xlsx')
html = response.read()

data1 = open_workbook(html)
laws = data1.sheet_by_index(0)
print laws
#
#lawlist=[]
#for law in range(laws.nrows):
#    lawlist.append(laws.row_values(law))
    
