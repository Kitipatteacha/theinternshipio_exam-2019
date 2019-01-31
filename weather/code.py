import json
import xmltodict
inputFile = "weather.xml"
file = open(inputFile, "r") 
xmlString = file.read()

print("Format XML")
print(xmlString)
     
jsonString = json.dumps(xmltodict.parse(xmlString,attr_prefix='',cdata_key=''),indent = 2)

print("Format json")

print(jsonString)
outputFile = "weather.json" 
file = open(outputFile, "w") 
file.write(jsonString)
