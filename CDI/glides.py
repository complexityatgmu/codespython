#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#open the xml file for reading:
files = open('data.xml','r')
#convert to string:
data = files.read()
#close file because we dont need it anymore:
files.close()
#parse the xml you got from the file
dom = parseString(data)

#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
xmlTag = dom.getElementsByTagName('event')[0].toxml()
#strip off the tag (<tag>data</tag>  --->   data):
xmlData=xmlTag.replace('<event>','').replace('</event>','')
#print out the xml tag and data in this format: <tag>data</tag>
print xmlTag
#just print the data
print xmlData
print xmlData