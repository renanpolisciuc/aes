import os
import sys
from xml.etree import ElementTree

def WriteInFile (writeFile, writeString):
  writeFile.write (writeString)


if len (sys.argv) < 2:
  print "[delayMedio.py] Missing arguments!"
  exit ()

traceFile = sys.argv[1]
xmlFile = sys.argv[1] + ".xml"
print "[delayMedio.py] Trace file: "+traceFile
print "[delayMedio.py] XML file: "+xmlFile
document = ElementTree.parse( xmlFile )

finalFile = open (traceFile, "a+")

for probe in document.findall( 'FlowProbes/FlowProbe' ):
  if probe.attrib [ 'index' ] == '2':
    for node in probe.getchildren ():
      sumDelay = node.attrib [ 'delayFromFirstProbeSum' ]
      sumDelay = (sumDelay)[1:len(sumDelay)-4]
      numPackets = node.attrib [ 'packets' ] 
      delayMedio = (float (sumDelay) / float (numPackets)) / 1000000000
      formatedDelayMedio = "{0:.4f}".format(delayMedio)
      print "[delayMedio] For "+node.attrib['flowId']+" delay average: "+formatedDelayMedio
      if node.attrib['flowId'] == '1':
	WriteInFile (finalFile, "delay_medio_lte="+formatedDelayMedio+"\n")
      else:
	WriteInFile (finalFile, "delay_medio_wifi="+formatedDelayMedio+"\n")
finalFile.close ()